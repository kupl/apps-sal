class Solution:

    def splitArraySameAverage(self, A: List[int]) -> bool:
        S = sum(A)
        N = len(A)
        A.sort(reverse=True)
        import functools

        @functools.lru_cache(None)
        def DFS(target, i, n_left):
            if target == 0:
                return n_left == 0
            if target < 0:
                return False
            if i == len(A):
                return False
            return DFS(target - A[i], i + 1, n_left - 1) or DFS(target, i + 1, n_left)
        return any((DFS(S * K // N, 0, K) for K in range(1, N) if S * K % N == 0))
