(n, t) = map(int, input().split())
a = [0] * (n + 1)
for i in range(n + 1):
    a[i] = [0] * (i + 1)
for i in range(t):
    a[0][0] += 1
    for j in range(n):
        for k in range(j + 1):
            if a[j][k] > 1:
                a[j + 1][k] += (a[j][k] - 1) / 2
                a[j + 1][k + 1] += (a[j][k] - 1) / 2
                a[j][k] = 1
res = 0
for j in range(n):
    for k in range(j + 1):
        if a[j][k] == 1:
            res += 1
print(res)
