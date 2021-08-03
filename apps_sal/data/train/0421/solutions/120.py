class Solution:
    def lastSubstring(self, s: str) -> str:
        l = []
        least = 'a'
        index = []
        for i, el in enumerate(s):
            if el == least:
                index.append(i)
            elif el > least:
                index = [i]
                least = el
        ans = ''
        for i in index:
            ans = max(ans, s[i:])
        return ans
