class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        mem = {}
        last = []
        for c in s:
            if not last or c != last[-1][0]:
                last.append([c, 0])
            last[-1][1] += 1
        if len(last) == 1:
            if k == len(s):
                return 0
            return len(''.join([x + (str(y - k) if y - k >= 2 else '') for x, y in last]))
        ns = ''.join([x + (str(y) if y >= 2 else '') for x, y in last])
        print(ns)

        def inner(i, lb, ll, ck):
            if ck < 0:
                return len(ns)
            if i == len(s):
                return 0
            if (i, lb, ll, ck) not in mem:
                mem[(i, lb, ll, ck)] = inner(i + 1, lb, ll, ck - 1)
                if s[i] == lb:
                    nll = ll + 1
                    if nll == 2 or nll == 10:
                        mem[(i, lb, ll, ck)] = min(mem[(i, lb, ll, ck)], inner(i + 1, lb, nll, ck) + 1)
                    else:
                        mem[(i, lb, ll, ck)] = min(mem[(i, lb, ll, ck)], inner(i + 1, lb, nll, ck))
                else:
                    mem[(i, lb, ll, ck)] = min(mem[(i, lb, ll, ck)], 1 + inner(i + 1, s[i], 1, ck))
            return mem[(i, lb, ll, ck)]
        print(mem)
        return inner(0, None, 0, k)
