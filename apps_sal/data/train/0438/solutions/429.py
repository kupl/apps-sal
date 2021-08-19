class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return m
        A = [i for i in range(n)]
        length = [0 for _ in range(n)]
        ans = -1

        def find(u):
            if u != A[u]:
                A[u] = find(A[u])
            return A[u]

        def union(u, v):
            (pu, pv) = (find(u), find(v))
            if pu == pv:
                return False
            A[max(pu, pv)] = min(pu, pv)
            length[min(pu, pv)] += length[max(pu, pv)]
        for (i, a) in enumerate(arr):
            a -= 1
            length[a] = 1
            for j in [a - 1, a + 1]:
                if 0 <= j < n:
                    if length[find(j)] == m:
                        ans = i
                    if length[j]:
                        union(j, a)
        return ans
