class Solution:

    def lastSubstring(self, s: str) -> str:
        n = len(s)
        cur = ord(s[0])
        indices = [0, 0]
        i = 1
        while i < n:
            if cur > ord(s[i]):
                indices[1] += 1
                i += 1
            elif cur < ord(s[i]):
                indices = [i, i]
                cur = ord(s[i])
                i += 1
            else:
                k = indices[0] + 1
                prev = i
                i += 1
                while k < prev and i < n:
                    if ord(s[k]) > ord(s[i]):
                        indices[1] = i
                        break
                    elif ord(s[i]) > cur:
                        indices = [i, i]
                        cur = ord(s[i])
                        break
                    elif ord(s[k]) < ord(s[i]):
                        print(prev, i)
                        indices = [prev, i]
                        break
                    i += 1
                    k += 1
                if i == n:
                    indices[1] = n - 1
                if k == prev:
                    indices[1] = i
        return s[indices[0]:indices[1] + 1]
