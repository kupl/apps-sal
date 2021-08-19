from collections import defaultdict


class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mapping = defaultdict(list)
        N = len(arr)
        for i in range(N):
            mapping[arr[i]].append(i)
        dp = [1] * N
        for i in range(1, N):
            curr = arr[i]
            if curr - difference in mapping:
                for idx in mapping[curr - difference]:
                    if idx >= i:
                        break
                    if dp[idx] + 1 > dp[i]:
                        dp[i] = dp[idx] + 1
        return max(dp)
