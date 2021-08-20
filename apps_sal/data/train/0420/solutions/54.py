class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        dict_vol = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        dict_vol = {x: 1 << y for (x, y) in dict_vol.items()}
        previous_seen = {0: -1}
        cur = 0
        ans = 0
        for (i, c) in enumerate(s):
            if c in dict_vol:
                cur = cur ^ dict_vol[c]
            if cur not in previous_seen:
                previous_seen[cur] = i
            else:
                ans = max(ans, i - previous_seen[cur])
        return ans
