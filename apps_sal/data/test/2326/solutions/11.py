def computeCnksMod(N, mod):
    res = [[0] * (N + 1) for i in range(N + 1)]
    res[0][0] = 1
    for n in range(1, N + 1):
        res[n][0] = res[n - 1][0]
        for k in range(1, n + 1):
            res[n][k] = (res[n - 1][k] + res[n - 1][k - 1]) % mod

    return res


magic = 998244353

n = int(input()) + 1
aa = [1] + [int(s) + 1 for s in input().split(' ')]

cnks = computeCnksMod(n, magic)

d = [0] * (n + 1)
d[n] = 1

for i in reversed(list(range(n))):
    if i != 0 and aa[i] < 2:
        continue

    cur = 0

    tosel = aa[i] - 1
    for j in range(i + tosel + 1, n + 1):
        avail = j - i - 1
        cur = (cur + cnks[avail][tosel] * d[j]) % magic

    d[i] = cur

print(d[0] - 1)
