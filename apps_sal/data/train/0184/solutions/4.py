class Solution:

    def maxRepOpt1(self, text: str) -> int:
        be = 1
        n = collections.Counter(text)
        maxl = 0
        i = 1
        re = []
        now = text[0]
        while i < len(text):
            if now == text[i]:
                be += 1
            if now != text[i] or i == len(text) - 1:
                res = be
                if len(re) >= 2:
                    print(re)
                    (com, lencom) = re.pop(0)
                    if re[-1][1] == 1 and com == now:
                        res = lencom + be
                if res < n[now]:
                    res += 1
                maxl = max(maxl, res)
                re.append((now, be))
                now = text[i]
                be = 1
            i += 1
        return maxl
