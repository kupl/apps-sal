def f(a):
    return a * (a + 1) // 2


(a, b, c) = map(int, input().split())
ans = f(a) * f(b) * f(c)
ans = ans % 998244353
print(ans)
