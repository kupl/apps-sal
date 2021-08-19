class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mp = collections.defaultdict(int)
        ans = 0
        for a in arr:
            mp[a] = max(1 + mp[a - difference], mp[a])
            ans = max(ans, mp[a])
        return ans
