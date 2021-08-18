class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        T = [0] * (N + 1)
        for i in range(1, N + 1):
            for j in range(1, k + 1):
                if j > i:
                    break
                T[i] = max(T[i], T[i - j] + max(arr[(i - j): i]) * j)
        return T[N]
