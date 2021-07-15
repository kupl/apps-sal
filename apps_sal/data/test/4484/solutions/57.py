n, m = list(map(int, input().split()))
if abs(n - m) > 1:
    print((0))
    return
ans = 1
for i in range(1, n + 1):
    ans *= i
    ans %= 10**9 + 7
for i in range(1, m + 1):
    ans *= i
    ans %= 10**9 + 7
if abs(n - m) == 0:
    ans *= 2
    ans %= 10**9 + 7
print(ans)

