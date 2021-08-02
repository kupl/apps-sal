n = int(input())
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

e = [[0] * n, [0] * n]
e1 = [[0] * n, [0] * n]
e2 = [[0] * n, [0] * n]
e[0][-1] = a[-1]
e[1][-1] = b[-1]
e1[0][-1] = (n - 1) * a[-1]
e1[1][-1] = (n - 1) * b[-1]

for j in range(2):
    for i in range(n - 2, -1, -1):
        e[j][i] += e[j][i + 1] + (a[i] if j == 0 else b[i])
        e1[j][i] += e1[j][i + 1] + (i) * (a[i] if j == 0 else b[i])
        e2[j][i] += e2[j][i + 1] + (n - i - 1) * (a[i] if j == 0 else b[i])

sum0 = e1[0][0] + e2[1][0] + e[1][0] * n

sum1 = 0
j = 1
for i in range(n - 1):
    sum1 += i * 2 * (a[i] + b[i]) + (b[i] if i % 2 == 0 else a[i])

    su = sum1
    su += e1[j][i + 1] + e2[j ^ 1][i + 1]
    su += e[j][i + 1] * (i + 1) + e[j ^ 1][i + 1] * (i + 1 + n)
    j ^= 1
    if su > sum0:
        sum0 = su

print(sum0)
