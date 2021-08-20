from sys import stdin, stdout


def rint():
    return map(int, stdin.readline().split())


(n, k, q) = rint()
r = [0 for i in range(200001)]
l = [0 for i in range(200001)]
for i in range(n):
    (ll, rr) = rint()
    r[rr] += 1
    l[ll] += 1
f = [0 for i in range(200001)]
for i in range(1, 200001):
    f[i] = f[i - 1] + l[i] - r[i - 1]
ss = [0 for i in range(200002)]
for i in range(200000, 0, -1):
    if f[i] >= k:
        ss[i] = ss[i + 1] + 1
    else:
        ss[i] = ss[i + 1]
for i in range(q):
    (ll, rr) = rint()
    print(ss[ll] - ss[rr + 1])
