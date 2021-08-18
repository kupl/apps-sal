n, m = map(int, input().split())

if abs(n - m) > 1:
    print(0)
    return

mod = 10**9 + 7
ans = 1
for i in range(1, n + 1):
    ans *= i
    ans %= mod
for i in range(1, m + 1):
    ans *= i
    ans %= mod
if (n + m) % 2 == 0:
    ans *= 2
    ans %= mod
print(ans)
