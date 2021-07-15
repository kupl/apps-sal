
# 1340. Jump Game V
# 20201003 这个题目，也只有用栈解决最快


class Solution:  # Decreasing Stack + DP （单调栈 DP）

    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [1] * (n + 1)
        stack = []
        for i, a in enumerate(arr + [float('inf')]):
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
    

