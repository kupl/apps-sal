import sys


def ii():
    return sys.stdin.readline().strip()


def idata():
    return [int(x) for x in ii().split()]


n = int(ii())
s = ii()
slov = {}
for i in range(97, 97 + 26):
    slov[chr(i)] = [[], [1]]
slov[s[0]] = [[1], [0, 0]]
for j in range(1, n):
    if slov[s[j]][1][-1] == 0:
        slov[s[j]][0][-1] += 1
    else:
        slov[s[j]][0] += [1]
        slov[s[j]][1] += [0]
    for i in range(97, 97 + 26):
        if chr(i) != s[j]:
            slov[chr(i)][1][-1] += 1
for t in range(int(ii())):
    (m, c) = ii().split()
    m = int(m)
    (a, b) = slov[c]
    if sum(b) <= m:
        print(n)
    elif not bool(a):
        print(m)
    elif len(a) == 1:
        print(a[0] + m)
    else:
        (l, r) = (0, 0)
        ans = 0
        (summ_a, summ_b) = (0, 0)
        used = 0
        b1 = b[:]
        (b1[0], b1[-1]) = (0, 0)
        count = 0
        while r != len(a):
            if summ_b + b1[r] <= m:
                summ_b += b1[r]
                summ_a += a[r]
                r += 1
                ans = max(ans, m + summ_a)
            else:
                summ_a -= a[l]
                l += 1
                summ_b -= b1[l]
        print(ans)
