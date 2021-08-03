n, m = list(map(int, input().split()))
p = 10**9 + 7
if abs(n - m) >= 2:
    print((0))
elif n == m:
    ans = 1
    for i in range(1, n + 1):
        ans = (ans * i) % p
    print(((2 * ans * ans) % p))
else:
    ans = 1
    for i in range(1, n + 1):
        ans = (ans * i) % p
    for i in range(1, m + 1):
        ans = (ans * i) % p
    print((ans % p))
