def permutation(n, k, mod):
    s = 1
    for _ in range(k):
        s *= n
        s %= mod
        n -= 1
    return s


def factorial(n, mod):
    s = 1
    for i in range(1, n + 1):
        s *= i
        s %= mod
    return s


h, w, a, b = map(int, input().split())
mod = pow(10, 9) + 7
x = h - a + b - 1
y = w - b + a - 2
p = permutation(x, h - a - 1, mod) * permutation(y, a - 1, mod) % mod
ans = p
for _ in range(w - b - 1):
    x += 1
    p = p * x * (y - (a - 1)) * pow((x - (h - a - 1)) * y, mod - 2, mod) % mod
    y -= 1
    ans += p
    ans %= mod
ans = ans * pow(factorial(a - 1, mod), mod - 2, mod) * pow(factorial(h - a - 1, mod), mod - 2, mod) % mod
print(ans)
