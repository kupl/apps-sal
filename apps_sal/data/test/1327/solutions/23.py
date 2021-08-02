n, m = list(map(int, input().split()))
p = [list(map(int, input().split())) for i in range(n)]
s = []
for i in range(8):
    s.append([])
    for j in range(n):
        x, y, z = p[j]
        sx = i // 4 % 2 * 2 - 1
        sy = i // 2 % 2 * 2 - 1
        sz = i % 2 * 2 - 1
        s[i].append(sx * x + sy * y + sz * z)
    s[i] = sorted(s[i], reverse=True)
ans = 0
for i in range(8):
    ans = max(ans, sum(s[i][:m]))
print(ans)
