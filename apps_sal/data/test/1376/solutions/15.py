def dist(x, xn):
    return max(x, xn) - min(x, xn)


n = int(input())
b = [[] for _ in range(n + 2)]
i = 1
for a in input().split():
    b[int(a)].append(i)
    i += 1
d = s = 1
res = 1
for a in range(1, n + 1):
    b[a].sort()
    dn, sn = b[a]
    res += dist(d, dn) + dist(s, sn)
    d, s = dn, sn
print(res - 1)

