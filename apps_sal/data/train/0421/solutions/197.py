class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        cur = ord(s[0])
        start = 0
        end = 0
        i = 1
        while i < n:
            if cur > ord(s[i]):
                end += 1
                i += 1
            elif cur < ord(s[i]):
                start, end = i, i
                cur = ord(s[i])
                i += 1
            else:
                k = start + 1
                prev = i
                i += 1
                while k < prev and i < n:
                    if ord(s[k]) > ord(s[i]):
                        end = i
                        break
                    elif ord(s[i]) > cur:
                        start, end = i, i
                        cur = ord(s[i])
                        break
                    elif ord(s[k]) < ord(s[i]):
                        start = prev
                        end = i
                        break
                    i += 1
                    k += 1
                if i == n:
                    end = n - 1
                if k == prev:
                    end = i
        return s[start:end + 1]
