n, m, c = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    tmp = 0
    a = list(map(int, input().split()))
    for j in range(m):
        tmp += a[j] * b[j]
    if tmp + c > 0:
        ans += 1

print(ans)
