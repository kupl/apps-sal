class Solution:
    def lastSubstring(self, s: str) -> str:

        char_max = max(s)
        ind = s.find(char_max)
        s = s[ind:]
        n = len(s)
        arr = [0] * n
        arr[-1] = s[-1]
        ans = arr[-1]
        for i in range(n - 2, -1, -1):
            if s[i] == char_max:
                if s[i:] > ans:
                    ans = s[i:]
        return ans
