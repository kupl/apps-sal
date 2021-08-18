class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        def find(parents, u):
            if u != parents[u]:
                parents[u] = find(parents, parents[u])

            return parents[u]

        def union(parents, ranks, u, v):
            pu = find(parents, u)
            pv = find(parents, v)
            if ranks[pu] >= ranks[pv]:
                parents[pv] = pu
                ranks[pu] += ranks[pv]
            else:
                parents[pu] = pv
                ranks[pv] += ranks[pu]

        n = len(arr)
        if n == m:
            return n

        laststep = -1
        parents = list(range(n))
        ranks = [0] * (n)
        for i in range(n):
            num = arr[i] - 1
            ranks[num] = 1
            if num - 1 >= 0:
                pleft = find(parents, num - 1)
                if ranks[pleft] == m:
                    laststep = i
                if ranks[pleft] > 0:
                    union(parents, ranks, num - 1, num)
            if num + 1 < n:
                pright = find(parents, num + 1)
                if ranks[pright] == m:
                    laststep = i
                if ranks[pright] > 0:
                    union(parents, ranks, num + 1, num)

        return laststep
