n, m, k = list(map(int, input().split()))
ans = 0
for i in range(k):
    ans += n * 2 + m * 2 - 4
    n -= 4
    m -= 4
print(ans)
