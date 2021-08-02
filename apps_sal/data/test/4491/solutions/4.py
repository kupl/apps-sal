n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]
cnt = 0
ans = 0
if n != 1:
    for i in range(1, n):
        cnt = sum(a[0][0:i]) + sum(a[1][i - 1:n])
        ans = max(ans, cnt)
        cnt = 0
else:
    ans = a[0][0] + a[1][0]
print(ans)
