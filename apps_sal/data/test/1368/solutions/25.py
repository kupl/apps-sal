N, A, B = list(map(int, input().split()))
v = list(map(int, input().split()))
v = sorted(v, reverse=True)

max_avg = (sum(v[:A]), A)

t = v[A - 1]
num1 = v[:A].count(t)
num2 = v[A:].count(t)

fact = [0] * (N + 1)
ifact = [0] * (N + 1)
inv = [0] * (N + 1)
p = 170141183460469231731687303715884105727


def combination(n, fact, ifact):
    fact[0] = 1
    fact[1] = 1
    ifact[0] = 1
    ifact[1] = 1
    inv[1] = 1
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % p
        inv[i] = p - inv[p % i] * (p // i) % p
        ifact[i] = (ifact[i - 1] * inv[i]) % p


def op(n, k):
    if k < 0 or k > n or n < 0:
        return 0
    return (fact[n] * ifact[k] * ifact[n - k]) % p


combination(N, fact, ifact)

res = int(op(num1 + num2, num1))
if v[0] == v[-1]:
    res = 0
    for i in range(A, B + 1):
        res += int(op(N, i))
elif v[0] == v[B - 1]:
    res = 0
    for i in range(A, B + 1):
        res += int(op(num1 + num2, i))
elif v[0] == v[A - 1]:
    res = 0
    for i in range(A, min(B, A + num2) + 1):
        res += int(op(num1 + num2, i))
print((max_avg[0] / max_avg[1]))
print(res)
