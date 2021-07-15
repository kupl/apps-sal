class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = 1
        table = {}
        for a in arr:
            prev = a - difference
            if prev in table:
                table[a] = table[prev] + 1
            else:
                table[a] = 1
            ans = max(ans, table[a])
        return ans

