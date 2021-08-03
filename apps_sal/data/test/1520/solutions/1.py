import sys
from collections import Counter
readline = sys.stdin.readline
N = int(readline())
S = [readline().strip() for i in range(N)]


def calc(s):
    res = []
    last = s[0]
    cnt = 0
    for c in s:
        if c == last:
            cnt += 1
        else:
            res.append((last, cnt))
            last = c
            cnt = 1
    if cnt > 0:
        res.append((last, cnt))
    return res


rr = calc(S[N - 1])
if len(rr) > 1:
    ans = max(x for c, x in rr)
    c0, x0 = rr[0]
    c1, x1 = rr[-1]
    m0 = m1 = 0
    for i in range(N - 1):
        s = S[i]
        for c in s:
            if c1 == c == c0:
                ans = max(ans, x0 + x1 + 1)
            elif c == c0:
                ans = max(ans, x0 + 1)
            elif c == c1:
                ans = max(ans, x1 + 1)
else:
    c0, x0 = rr[0]
    rr0 = calc(S[0])
    r = 0
    for c, x in rr0:
        if c0 == c:
            r = max(r, x)
    for i in range(1, N - 1):
        rr1 = calc(S[i])
        if len(rr1) == 1:
            c1, x1 = rr1[0]
            if c0 == c1:
                r = (r + 1) * x1 + r
            else:
                r = +(r > 0)
        else:
            d0, y0 = rr1[0]
            d1, y1 = rr1[-1]
            if c0 != d0:
                y0 = 0
            if c0 != d1:
                y1 = 0
            if r > 0:
                r = y0 + y1 + 1
            else:
                r = max(y0, y1)
            for d, y in rr1:
                if d == c0:
                    r = max(r, y)
    ans = (r + 1) * x0 + r
print(ans)
