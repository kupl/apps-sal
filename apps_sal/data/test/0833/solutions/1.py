(n, v) = [int(i) for i in input().split()]
a = [0] * n
b = [0] * n
days1 = [0] * 3001
days2 = [0] * 3001
for i in range(n):
    (a[i], b[i]) = [int(j) for j in input().split()]
    days1[a[i] - 1] += b[i]
    days2[a[i]] += b[i]
res = 0
for i in range(3001):
    left = max(0, v - days2[i])
    res += max(0, min(v, days2[i]))
    res += min(left, days1[i])
    if i != 3000:
        days2[i + 1] -= min(left, days1[i])
print(res)
