import math
mod = 10 ** 9 + 7


def fact(s, k):
    f = math.factorial(s - 2 * k - 1) // math.factorial(s - 3 * k)
    f //= math.factorial(k - 1)
    return f % mod


s = int(input())

ans = 0
for i in range(1, s // 3 + 1):
    ans += fact(s, i)
ans %= mod

print(ans)
