(n, d) = map(int, input().split())
xy = []
for _ in range(n):
    s = [int(i) for i in input().split()]
    xy.append(s)
ans = 0
for s in xy:
    if s[0] ** 2 + s[1] ** 2 <= d ** 2:
        ans += 1
print(ans)
