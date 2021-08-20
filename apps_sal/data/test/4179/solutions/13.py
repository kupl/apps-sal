(n, m, c) = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
sum_tmp = 0
for i in range(n):
    for j in range(m):
        sum_tmp += a[i][j] * b[j]
    else:
        if sum_tmp + c > 0:
            ans += 1
        sum_tmp = 0
print(ans)
