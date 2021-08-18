import sys

mod = 998244353


def mult(a, b):
    y = 1
    for i in range(b):
        y = y * a % mod
    return y


def getS(cnt, k, b1, b2):
    if b1 < b2:
        b1, b2 = b2, b1
    if b1 == b2 == 0:
        s = mult(k - 1, cnt - 1)
        s = s * k % mod
        return s
    if b2 == 0:
        return mult(k - 1, cnt)
    re = [k - 1] * cnt
    for i in range(1, cnt):
        re[i] = re[i - 1] * (k - 1) % mod
    re[0] = k - (1 if b1 == b2 else 2)
    # print(re)
    tot = 0
    mm = 1
    for i in range(cnt - 1, -1, -1):
        tot += mm * re[i]
        mm *= -1
        tot = (tot + mod) % mod
    return tot


def solve(x, k):
    n = len(x)
    x = [0] + x + [0]
    st = -1
    rt = 1
    for i in range(n + 2):
        if x[i] != -1:
            if st != -1:
                rt = (rt * getS(i - st, k, x[st - 1], x[i])) % mod
            st = -1
        else:
            if st == -1:
                st = i
    return rt


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
for i in range(0, n - 2):
    if a[i] != -1 and a[i] == a[i + 2]:
        print(0)
        return
even = solve(a[::2], k)
odd = solve(a[1::2], k)
print(even * odd % mod)
