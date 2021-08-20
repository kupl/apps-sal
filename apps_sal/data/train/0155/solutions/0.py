class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = [1] * (len(arr) + 1)
        stack = []
        for (i, n) in enumerate(arr + [1000000]):
            while stack and arr[stack[-1]] < n:
                same_height_idx = [stack.pop()]
                while stack and arr[stack[-1]] == arr[same_height_idx[0]]:
                    same_height_idx.append(stack.pop())
                for j in same_height_idx:
                    if i - j <= d:
                        dp[i] = max(dp[i], dp[j] + 1)
                    if stack and j - stack[-1] <= d:
                        dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)
            stack.append(i)
        return max(dp[:-1])
