class Solution:
    def lastSubstring(self, s: str) -> str:
        for i,c in enumerate(s):
            if i == 0:
                max_c = c
                max_id=[i]
            else:
                if c > max_c:
                    max_id = [i]
                    max_c = c
                elif c == max_c:
                    max_id.append(i)
        max_substr = s[max_id[0]:]
        for idx in max_id:
            if s[idx:] > max_substr:
                max_substr = s[idx:]
        return max_substr

