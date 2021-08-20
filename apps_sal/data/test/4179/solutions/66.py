(n, m, c) = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
for i in range(n):
    a = list(map(int, input().split()))
    cntt = 0
    for j in range(m):
        cntt += a[j] * b[j]
    if cntt + c > 0:
        cnt += 1
print(cnt)
