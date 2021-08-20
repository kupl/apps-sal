(n, m, c) = map(int, input().split())
b = list(map(int, input().split()))
cnt = 0
for i in range(n):
    pro = c
    a = list(map(int, input().split()))
    for j in range(m):
        pro += a[j] * b[j]
    if pro > 0:
        cnt += 1
print(cnt)
