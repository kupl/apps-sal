class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(' ')
        ans = ""

        for segment in s.split(' '):
            if segment == '':
                continue
            ans = segment + " " + ans

        return ans[:-1]
