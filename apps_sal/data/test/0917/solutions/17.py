def getn():
    return int(input())


def getns():
    return [int(x) for x in input().split()]


(n, h, m) = getns()
hs = [h] * (n + 1)
for i in range(m):
    (l, r, x) = getns()
    for i in range(l, r + 1):
        hs[i] = min(hs[i], x)
ans = 0
for i in range(1, n + 1):
    ans += hs[i] * hs[i]
print(ans)
