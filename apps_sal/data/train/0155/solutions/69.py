class Solution2:

    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [1] * n
        for (a, i) in sorted(([a, i] for (i, a) in enumerate(arr))):
            for di in [-1, 1]:
                for j in range(i + di, i + di + d * di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution:

    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [1] * (n + 1)
        stack = []
        for (i, a) in enumerate(arr + [float('inf')]):
            while stack and arr[stack[-1]] < a:
                L = [stack.pop()]
                while stack and arr[stack[-1]] == arr[L[0]]:
                    L.append(stack.pop())
                for j in L:
                    if i - j <= d:
                        dp[i] = max(dp[i], dp[j] + 1)
                    if stack and j - stack[-1] <= d:
                        dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)
            stack.append(i)
        return max(dp[:-1])


class Solution1:

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        res = [0] * n

        def dp(i):
            if res[i]:
                return res[i]
            res[i] = 1
            for di in [-1, 1]:
                for j in range(i + di, i + di + d * di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    res[i] = max(res[i], dp(j) + 1)
            return res[i]
        return max(list(map(dp, list(range(n)))))
