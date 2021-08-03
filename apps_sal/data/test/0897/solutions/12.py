def f():
    nonlocal MOD, ans, factor
    ans %= MOD
    factor %= MOD


MOD = 10**9 + 7

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

reverse = pow(m, MOD - 2, MOD)
reverse_for_2 = (MOD + 1) // 2
ans = 0
factor = 1
for a, b in zip(a, b):
    if (a == b == 0):
        ans += factor * ((m - 1) * (reverse * reverse_for_2))
        factor *= reverse
        f()
    elif (a == 0):
        ans += factor * (m - b) * reverse
        factor *= reverse
        f()
    elif (b == 0):
        ans += factor * (a - 1) * reverse
        factor *= reverse
        f()
    elif (a > b):
        ans += factor
        f()
        break
    elif (a == b):
        pass
    elif (a < b):
        break
f()
print(ans)
