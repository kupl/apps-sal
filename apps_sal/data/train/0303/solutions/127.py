class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        DP = [0 for _ in range(len(arr) + 1)]
        for i in range(1, len(DP)):
            loc = max(i - k, 0)
            run_max = 0
            for j in range(loc, i):
                run_max = max(run_max, DP[j] + max(arr[j:i]) * (i - j))
            DP[i] = run_max
        return DP[-1]
