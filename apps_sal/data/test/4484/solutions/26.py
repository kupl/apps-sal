MOD = 1000000007
(n, m) = map(int, input().split())
if abs(n - m) > 1:
    print(0)
else:
    if abs(n - m) == 1:
        ans = 1
    else:
        ans = 2
    for i in range(n):
        ans = ans * (i + 1) % MOD
    for i in range(m):
        ans = ans * (i + 1) % MOD
    print(ans)
