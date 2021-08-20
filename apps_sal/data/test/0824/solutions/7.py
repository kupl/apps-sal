mod = 10 ** 9 + 7
maxn = 200001


def C(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * invfact[k] * invfact[n - k] % mod


fact = [1, 1]
inv = [0, 1]
invfact = [1, 1]
for i in range(2, maxn):
    fact.append(fact[-1] * i % mod)
    inv.append(inv[mod % i] * (mod - mod // i) % mod)
    invfact.append(invfact[-1] * inv[-1] % mod)
s = input()
op = 0
cl = s.count(')')
ans = 0
for x in s:
    if x == '(':
        op += 1
        cur = C(cl + op - 1, op) % mod
        ans += cur % mod
    else:
        cl -= 1
print(ans % mod)
