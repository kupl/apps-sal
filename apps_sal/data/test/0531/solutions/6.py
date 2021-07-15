import itertools
from collections import Counter

def from_edges(a, b, c):
    m = min(a, c)
    ap = a - m
    bp = 2 * m + b
    cp = c - m
    return ap, bp, cp

def to_edges(a, b, c):
    h = b // 2
    ap = a + h
    bp = b - 2 * h
    cp = c + h
    return ap, bp, cp

def score(a, b, c, ap, bp, cp):
    return min(a, ap) + min(b, bp) + min(c, cp)

def gen_ans(s, ap, bp, cp):
    return itertools.chain(
        itertools.repeat(s - 1, ap),
        itertools.repeat(s, bp),
        itertools.repeat(s + 1, cp)
    )

n = int(input())
inp = input()
cnt = Counter(int(v) for v in inp.split())
items = sorted(cnt.items())

if len(items) == 1:
    print(n)
    print(inp)
    return
elif len(items) == 2:
    if items[1][0] - items[0][0] == 1:
        print(n)
        print(inp)
        return
    else:
        # diff is 2
        a, b, c = items[0][1], 0, items[1][1]
        s = items[0][0] + 1
        ap, bp, cp = from_edges(a, b, c)
        print(score(a, b, c, ap, bp, cp))
        print(' '.join(str(v) for v in gen_ans(s, ap, bp, cp)))
else:
    a, b, c = [p[1] for p in items]
    s = items[1][0]
    ap1, bp1, cp1 = from_edges(a, b, c)
    ap2, bp2, cp2 = to_edges(a, b, c)
    score1 = score(a, b, c, ap1, bp1, cp1)
    score2 = score(a, b, c, ap2, bp2, cp2)
    if score1 <= score2:
        ap, bp, cp, score = ap1, bp1, cp1, score1
    else:
        ap, bp, cp, score = ap2, bp2, cp2, score2
    print(score)
    print(' '.join(str(v) for v in gen_ans(s, ap, bp, cp)))

