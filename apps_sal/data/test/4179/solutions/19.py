n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = []
cnt = 0

for i in range(n):
    a.append(list(map(int, input().split())))
    tmp = 0
    for j in range(m):
        tmp += a[i][j] * b[j]
    if tmp + c > 0:
        cnt += 1

print(cnt)
