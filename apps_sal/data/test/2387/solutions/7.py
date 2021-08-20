import sys
input = sys.stdin.readline


def check(s):
    h = 0
    for p in s:
        b = h + p[0]
        if b < 0:
            return False
        h += p[1]
    return True


N = int(input())
S = [input().strip() for i in range(N)]
total = 0
(ps, ms) = ([], [])
for s in S:
    (h, b) = (0, 0)
    for c in s:
        if c == '(':
            h += 1
        else:
            h -= 1
        b = min(b, h)
    if h > 0:
        ps.append([b, h])
    else:
        ms.append([b - h, -h])
    total += h
ps.sort(reverse=True)
ms.sort(reverse=True)
if check(ps) and check(ms) and (total == 0):
    print('Yes')
else:
    print('No')
