n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
sum = 0

for i in range(m):
    for j in range(n):
        sum += b[i] * a[j][i]

for j in range(n):
    sum = 0
    for i in range(m):
        sum += b[i] * a[j][i]
    if sum + c > 0:
        cnt += 1

print(cnt)
