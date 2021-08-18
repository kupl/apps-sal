x, y = list(map(int, input().split()))

if (x + y) % 3 != 0 or x * 2 < y or y * 2 < x:
    print((0))
    return

a = (2 * x - y) // 3
b = (2 * y - x) // 3

# ans = math.factorial(a+b)/math.factorial(a)
# ans=1
# for i in range(a+1,a+b+1):
#     ans*=i%(10**9+7)


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 10 ** 9 + 7
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans = cmb(a + b, a, p)

print(ans)
