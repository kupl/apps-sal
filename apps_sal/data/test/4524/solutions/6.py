input()
a = list(map(int, input()))
b = list(map(int, input()))

mod = 998244353


def binpow(a, n):
    if n == 0:
        return 1
    ans = binpow(a, n // 2)
    ans = (ans * ans) % mod
    if n % 2 == 1:
        ans = (ans * a) % mod
    return ans


c = 1
ans = 0
s = sum(b)
for i in range(min(len(a), len(b))):
    if a[-1 - i] == 1:
        ans = (ans + c * s) % mod
    s -= b[-1 - i]
    c = (c * 2) % mod
print(ans)
