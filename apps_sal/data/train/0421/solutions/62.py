class Solution:

    def lastSubstring(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = []
        max_char = s[0]
        res.append(0)
        i = 1
        while i <= len(s) - 1:
            if s[i] > max_char:
                res = [i]
                max_char = s[i]
            elif s[i] == max_char:
                if s[i - 1] != max_char:
                    res.append(i)
            i += 1
        while len(res) > 1:
            p0 = res[0]
            p1 = res[1]
            count = 1
            while p0 + count < p1:
                if p1 + count > len(s) - 1:
                    return s[res[0]:]
                if s[p0 + count] > s[p1 + count]:
                    res.pop(1)
                    break
                elif s[p0 + count] < s[p1 + count]:
                    res.pop(0)
                    break
                else:
                    count += 1
            if p0 + count == p1:
                res.pop(1)
        return s[res[0]:]
