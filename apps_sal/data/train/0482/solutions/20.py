class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        def compute(arr, lo, hi, dp):
            if dp[lo][hi] != -1:
                return dp[lo][hi]
            if hi == lo:
                dp[lo][hi] = 0, arr[lo]
                return 0, arr[lo]
            if hi == lo + 1:
                dp[lo][hi] = arr[lo] * arr[hi], max(arr[lo], arr[hi])
                return arr[lo] * arr[hi], max(arr[lo], arr[hi])

            k = float('inf')
            c = 0
            for i in range(lo, hi):
                left = compute(arr, lo, i, dp)
                right = compute(arr, i + 1, hi, dp)
                t = left[0] + right[0] + left[1] * right[1]
                if t < k:
                    k = t
                    c = max(left[1], right[1])
            dp[lo][hi] = k, c
            return k, c

        dp = [[-1] * len(arr) for row in arr]

        x = compute(arr, 0, len(arr) - 1, dp)
        print(dp)
        return x[0]
