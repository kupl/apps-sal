class Solution:

    def splitArraySameAverage(self, A: List[int]) -> bool:
        S = sum(A)
        N = len(A)
        A.sort()
        import functools

        @functools.lru_cache(None)
        def DFS(target, i, n_left):
            if target == 0:
                return n_left == 0
            if i == len(A) or target < 0 or target - A[i] * n_left < 0:
                return False
            return DFS(target - A[i], i + 1, n_left - 1) or DFS(target, i + 1, n_left)
        return any((DFS(S * K // N, 0, K) for K in range(1, N) if S * K % N == 0))
