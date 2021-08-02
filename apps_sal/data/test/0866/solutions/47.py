x, y = map(int, input().split())
mod = 10**9 + 7
flflag = True

if (2 * x - y) % 3 == 0:
    a = (2 * x - y) // 3
else:
    flflag = False
if (2 * y - x) % 3 == 0:
    b = (2 * y - x) // 3
else:
    flflag = False


def kaijou(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i % mod
        ans %= mod
    return ans


if flflag:
    N = a + b
    R = min(a, b)
ans = 0
if flflag == True and a >= 0 and b >= 0:
    ans = kaijou(N)
    ans1 = (kaijou(N - R) * kaijou(R)) % mod
    print((ans * pow(ans1, mod - 2, mod)) % mod)
else:
    print(0)
