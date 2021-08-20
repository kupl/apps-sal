def mod1(x):
    mod = 10 ** 9 + 7
    ans = 1
    y = 1
    while y <= x:
        ans = ans * y
        y += 1
        ans = ans % mod
    return ans % mod


(n, m) = map(int, input().split())
if n == m:
    print(2 * mod1(n) * mod1(m) % (10 ** 9 + 7))
elif abs(n - m) == 1:
    print(mod1(n) * mod1(m) % (10 ** 9 + 7))
else:
    print(0)
