def f(n):
    if n == 0:
        return 0
    return 2 ** (n - 1) + 2 * f(n - 1)


f = [0] * 60
for n in range(1, 60):
    f[n] = 2 ** (n - 1) + 2 * f[n - 1]
n = int(input())
ans = 0
for k in range(60, 0, -1):
    if n >= 2 ** k:
        ans += f[k]
        n -= 2 ** k
        if n > 0:
            ans += 2 ** k
print(int(ans))
