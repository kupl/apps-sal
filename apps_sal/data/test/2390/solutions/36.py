# 095_D
n, c = map(int, input().split())
x, v = [0], [0]
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    v.append(b)
x.append(c)
v.append(0)

fr1, fr2 = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
fl1, fl2 = [0 for _ in range(n + 2)], [0 for _ in range(n + 2)]

tmp1, tmp2 = 0, 0
for i in range(0, n):
    tmp1 += v[i + 1] - (x[i + 1] - x[i])
    tmp2 += v[i + 1] - 2 * (x[i + 1] - x[i])
    fr1[i + 1] = max(tmp1, fr1[i])
    fr2[i + 1] = max(tmp2, fr2[i])

tmp1, tmp2 = 0, 0
for i in range(n, 0, -1):
    tmp1 += v[i] - abs(x[i + 1] - x[i])
    tmp2 += v[i] - 2 * abs(x[i + 1] - x[i])
    fl1[i] = max(tmp1, fl1[i + 1])
    fl2[i] = max(tmp2, fl2[i + 1])

ans = 0
for i in range(n + 1):
    ans = max(ans, fr1[i] + fl2[i + 1], fr2[i] + fl1[i + 1])
print(ans)
