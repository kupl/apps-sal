class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        cnt = collections.Counter()
        ans = 0
        for num in arr:
            cnt[num] = cnt[num - difference] + 1
            ans = max(ans, cnt[num])
        return ans
