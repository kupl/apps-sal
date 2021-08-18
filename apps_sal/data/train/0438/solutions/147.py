class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        parents = [-1] * n
        ranks = [0] * n
        if m == n:
            return m
        ans = -1

        def find(n):
            if parents[n] >= 0:
                parents[n] = find(parents[n])
            else:
                return n
            return parents[n]

        def union(m, n):
            pm, pn = find(m), find(n)
            if ranks[pm] > ranks[pn]:
                parents[pn] = pm
                ranks[pm] += ranks[pn]
            else:
                parents[pm] = pn
                ranks[pn] += ranks[pm]
            return True
        visited = set([])
        for i, a in enumerate(arr):
            a -= 1
            ranks[a] = 1
            for j in [a - 1, a + 1]:
                if 0 <= j < n:
                    if ranks[find(j)] == m:
                        ans = i
                    if j in visited:
                        union(a, j)
            visited.add(a)
        return ans
