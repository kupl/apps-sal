n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
count = 0
tmp = 0
for i in range(n):
    for j in range(m):
        tmp += a[i][j] * b[j]
    count += 1 if tmp + c > 0 else 0
    tmp = 0
print(count)
