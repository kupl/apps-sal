n, m = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
ans = 0
for i in range(n):
    r = l[i]
    c1 = r.count(1)
    c2 = r.count(0)
    ans += (((2**c1) - 1) + ((2**c2) - 1))
for i in range(m):
    ls = []
    for j in range(n):
        ls.append(l[j][i])
    c1 = ls.count(1)
    c2 = ls.count(0)
    ans += (((2**c1) - 1) + ((2**c2) - 1) - c1 - c2)
print(ans)
