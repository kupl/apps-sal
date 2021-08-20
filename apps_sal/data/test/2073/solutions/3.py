n = int(input())
l = list(map(int, input().split()))
l.insert(0, 0)
mark = {}
(loop, pos, res, mod) = (0, 1, 1, int(1000000000.0 + 7))
for i in range(1, n + 1):
    if not i in mark:
        (start, j) = (pos, i)
        while not j in mark:
            mark[j] = pos
            pos += 1
            j = l[j]
        if mark[j] >= start:
            size = pos - mark[j]
            loop += size
            res *= pow(2, size) - 2 + mod
            res %= mod
res = res * pow(2, n - loop, mod) % mod
print(res)
