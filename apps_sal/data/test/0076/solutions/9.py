n, m, a, b = list(map(int, input().split()))
ans = 100000000000000000000
if n % m == 0:
    ans = 0
k = n % m
ans = min(ans, k * b, (m - k) * a)


print(ans)
