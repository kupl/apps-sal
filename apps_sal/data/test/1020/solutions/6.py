n, m, k = map(int, input().split())
ans = 0
while (k > 0 and n > 0 and m > 0):
    ans += (n + m - 2) * 2
    n -= 4
    m -= 4
    k -= 1
print(ans)
