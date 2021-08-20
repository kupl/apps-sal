import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
(ls, rs) = ([], [])
total = 0
for i in range(n):
    s = input()
    (h, b) = (0, 0)
    for c in s:
        if c == '(':
            h += 1
        else:
            h -= 1
        b = min(b, h)
    if h > 0:
        ls.append((b, h))
    else:
        rs.append((b - h, -h))
    total += h
ls.sort(reverse=True)
rs.sort(reverse=True)


def chk(s):
    h = 0
    for (sb, sh) in s:
        b = h + sb
        if b < 0:
            return False
        h += sh
    return True


if chk(ls) and chk(rs) and (total == 0):
    print('Yes')
else:
    print('No')
