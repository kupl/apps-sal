class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = [1] * len(arr)
        a = []
        for (idx, val) in enumerate(arr):
            a.append((val, idx))
        a.sort()
        print(a)
        for (_, idx) in a:
            for i in range(1, d + 1):
                if idx + i < len(arr) and arr[idx + i] < arr[idx]:
                    dp[idx] = max(dp[idx], dp[idx + i] + 1)
                else:
                    break
            for i in range(1, d + 1):
                if 0 <= idx - i and arr[idx - i] < arr[idx]:
                    dp[idx] = max(dp[idx], dp[idx - i] + 1)
                else:
                    break
        return max(dp)
