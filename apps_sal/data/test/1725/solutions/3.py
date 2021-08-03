n, m, d = (int(x) for x in input().split())
s = set()
l = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    s |= {x % d for x in tmp}
    l += [x // d for x in tmp]
if len(s) != 1:
    print(-1)
    return
l.sort()
mean = l[n * m // 2]
ans = 0
for x in l:
    ans += abs(x - mean)
if n * m // 2 > 0:
    mean = l[n * m // 2 - 1]
    ans2 = 0
    for x in l:
        ans2 += abs(x - mean)
    ans = min(ans, ans2)
print(ans)
