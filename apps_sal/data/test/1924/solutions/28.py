r1, c1, r2, c2 = list(map(int, input().split()))
n = 2 * max(r1, r2, c1, c2) + 2
mod = 10**9 + 7

factorial = [1]
for i in range(1, n + 1):
    factorial.append(factorial[-1] * i % mod)

inv_factorial = [-1] * (n + 1)
inv_factorial[-1] = pow(factorial[-1], mod - 2, mod)
for i in reversed(list(range(n))):
    inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % mod


def fact(n):
    return factorial[n]


def nck(n, k):
    if k > n or k < 0:
        return 0
    else:
        return factorial[n] * inv_factorial[n - k] * inv_factorial[k]


def routes(r, c):
    return nck(r + c + 2, c + 1) - 1


ans = routes(r2, c2) - routes(r2, c1 - 1) - routes(c2, r1 - 1) + routes(r1 - 1, c1 - 1)
ans %= mod
print(ans)
