class Solution:
    def lastSubstring(self, s: str) -> str:
        cand = list(range(len(s)))
        ans = ''
        step = 0
        while len(cand) > 1:
            nxt = []
            tmp = None
            for x in cand:
                if tmp is None or ord(s[x]) > ord(tmp):
                    tmp = s[x]
            ans += tmp
            for x in cand:
                if tmp == s[x]:
                    if x + 1 < len(s) and (len(nxt) == 0 or nxt[-1] < x - step):
                        nxt.append(x + 1)
            cand = nxt
            step += 1
        if len(cand) == 0:
            return ans
        return ans + s[cand[0]:]
