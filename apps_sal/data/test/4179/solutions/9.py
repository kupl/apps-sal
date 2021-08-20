(n, m, c) = map(int, input().split())
b = list(map(int, input().split()))
cnt = 0
for i in range(n):
    ac = 0
    a = list(map(int, input().split()))
    for j in range(m):
        ac += a[j] * b[j]
    if ac + c > 0:
        cnt += 1
print(cnt)
