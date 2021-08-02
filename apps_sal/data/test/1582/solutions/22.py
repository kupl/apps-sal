n = int(input())
a = [[0 for j in range(10)] for i in range(10)]

for i in range(1, n + 1):
    if i >= 10**5:
        tmp1 = i // 10**5
    elif i >= 10**4:
        tmp1 = i // 10**4
    elif i >= 10**3:
        tmp1 = i // 10**3
    elif i >= 10**2:
        tmp1 = i // 10**2
    elif i >= 10:
        tmp1 = i // 10
    else:
        tmp1 = i
    tmp2 = i % 10
    a[tmp1][tmp2] += 1

cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        cnt += a[i][j] * a[j][i]
print(cnt)
