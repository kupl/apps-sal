class Solution:

    def maxJumps2(self, arr: List[int], d: int) -> int:
        n = len(arr)
        res = [0] * n

        def dp(i):
            if res[i] > 0:
                return res[i]
            res[i] = 1
            for di in [-1, 1]:
                for j in range(i + di, i + d * di + di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    res[i] = max(res[i], dp(j) + 1)
            return res[i]
        return max(map(dp, range(n)))

    def maxJumps1(self, arr, d):
        n = len(arr)
        res = [0] * n

        def dp(i):
            if res[i] > 0:
                return res[i]
            res[i] = 1
            for j in range(i + 1, i + d + 1):
                if j >= n or arr[j] >= arr[i]:
                    break
                res[i] = max(res[i], dp(j) + 1)
            for j in range(i - 1, i - d - 1, -1):
                if j < 0 or arr[j] >= arr[i]:
                    break
                res[i] = max(res[i], dp(j) + 1)
            return res[i]
        return max((dp(i) for i in range(n)))

    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [1] * n
        for (a, i) in sorted(([a, i] for (i, a) in enumerate(arr))):
            for di in [-1, 1]:
                for j in range(i + di, i + d * di + di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
