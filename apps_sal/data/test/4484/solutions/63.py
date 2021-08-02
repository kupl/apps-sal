n, m = list(map(int, input().split()))
if n > m:
    n, m = m, n
ans = 1
if m == n:

    while n > 0:
        ans *= n
        ans %= 10**9 + 7
        n -= 1
    ans = (2 * (ans**2)) % (10**9 + 7)
    print(ans)

elif m - n == 1:
    while n > 0:
        ans *= n
        ans %= 10**9 + 7
        n -= 1

    ans = (ans * (ans * m % (10**9 + 7))) % (10**9 + 7)
    print(ans)
else:
    print((0))
