(a, b, f, k) = list(map(int, input().split()))
fuel = b - f
(c, d) = (0, [a - f << 1, f << 1])
flag = 1
for i in range(k):
    if fuel < 0:
        flag = 0
        break
    dis = d[i & 1] * (1 if i != k - 1 else 0.5)
    if fuel < dis:
        fuel = b
        c += 1
    fuel -= dis
if fuel < 0:
    flag = 0
print(c if flag else '-1')
