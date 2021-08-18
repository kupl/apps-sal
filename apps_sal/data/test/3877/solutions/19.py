from collections import defaultdict


def ri():
    return map(int, input().split())


pt = defaultdict()
ln = defaultdict()

n, l, r = ri()


def lenn(n):
    if n in ln:
        return ln[n]
    if n == 1:
        ln[1] = 1
        return 1
    elif n == 0:
        ln[0] = 1
        return 1
    i = 2 * lenn(n // 2) + 1
    ln[n] = i
    return i


def pn(n):
    if n in pt:
        return pt[n]
    pt[n] = 1 + lenn(n) // 2
    return pt[n]


def findval(i, p, n):
    if p == i:
        return n % 2
    if p > i:
        return findval(i, p - pn(n // 2), n // 2)
    else:
        return findval(i, p + pn(n // 2), n // 2)


ans = 0
p = pn(n)
for i in range(l, r + 1):
    ans += findval(i, p, n)

print(ans)
