class Solution:
    def lastSubstring(self, s: str) -> str:
        ans = s[0]
        for i in range(len(s)):
            if s[i] < ans[0]:
                continue
            else:

                # for j in range(i, len(s)):
                #     if s[i:j+1]>ans:
                ans = max(s[i:], ans)
        return ans
