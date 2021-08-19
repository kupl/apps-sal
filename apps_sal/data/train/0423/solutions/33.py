class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mp = collections.defaultdict(int)
        ans = 0
        for a in arr:
            mp[a] = 1 + mp[a - difference]
            ans = max(ans, mp[a])
        return ans
