class Solution:

    def lastSubstring(self, s: str) -> str:
        biggest = max(s)
        start_ids = []
        for (i, letter) in enumerate(s):
            if letter == biggest:
                start_ids.append(i)
        ans = s
        for i in start_ids:
            ans = max(ans, s[i:])
        return ans
