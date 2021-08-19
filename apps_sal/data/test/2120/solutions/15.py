(n, m) = map(int, input().split())
v = [int(elm) for elm in input().split()]
ans = 0
for i in range(m):
    (x, y) = map(int, input().split())
    ans += min(v[x - 1], v[y - 1])
print(ans)
