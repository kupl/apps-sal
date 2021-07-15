n, m, k = list(map(int, input().split()))
if n < m:
    n, m = m, n
if k == -1:
    if (n % 2 == 0 and m % 2 == 1) or (n % 2 == 1 and m % 2 == 0):
        ans = 0
    else:
        ans = pow(2, (n - 1) * (m - 1), 1000000007)
else:
    ans = pow(2, (n - 1) * (m - 1), 1000000007)
print(ans)
