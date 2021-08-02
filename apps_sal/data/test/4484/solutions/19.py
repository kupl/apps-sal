n, m = list(map(int, input().split()))

mod = 10**9 + 7
ans = 1


if abs(n - m) >= 2:
    ans = 0
elif abs(n - m) == 1:
    for i in range(1, max(n, m) + 1):
        ans *= i
        ans %= mod
    for j in range(1, min(n, m) + 1):
        ans *= j
        ans %= mod
elif abs(n - m) == 0:
    for i in range(1, n + 1):
        ans *= i
        ans %= mod
    ans **= 2
    ans *= 2
    ans %= mod


print(ans)
