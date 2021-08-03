M = 998244353


def fact(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
        ans %= M
    return ans


n = int(input())


x = fact(n)
ans = x - n
k = n
for i in range(1, n + 1):
    ans += x - k * (n - i)
    ans %= M
    k *= (n - i)
    k %= M
print(ans)
