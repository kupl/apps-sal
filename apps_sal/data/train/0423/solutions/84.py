class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        mp = {}
        ans = 0
        for n in arr:
            prev = mp.get(n,0)
            if n-diff in mp:
                mp[n] = mp[n-diff] + 1
            else:
                mp[n] = 1
            mp[n] = max(prev, mp[n])
            ans = max(ans, mp[n])
        return ans
