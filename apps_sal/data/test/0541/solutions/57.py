n, m = list(map(int, input().split()))
p = []
for _ in range(m):
    a, b = list(map(int, input().split()))
    p.append([a, b])
p.sort(key=lambda x: x[1])
ans = 0
cur = 0
for i in range(m):
    if cur <= p[i][0]:
        ans += 1
        cur = p[i][1]
print(ans)
