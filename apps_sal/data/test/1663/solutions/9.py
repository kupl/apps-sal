s = [int(c) for c in input()][::-1]
n = len(s)
mod = 1000000007


def inv(x):
    return pow(x, mod - 2, mod)


teninv = inv(10)
P = [0]
p = 1
for x in s:
    P.append((P[-1] + x * p) % mod)
    p = p * 10 % mod
Q = [0]
for i in range(n + 1):
    Q.append((Q[-1] + P[i] * pow(teninv, i, mod)) % mod)
s = 0
for l in range(n):
    first = P[l] - P[0]
    s += (n - l) * first % mod
    s += P[n] * inv(9) % mod * (1 - inv(pow(10, n - l, mod))) % mod
    d = Q[n + 1] - Q[l + 1]
    s = (s - d * inv(pow(teninv, l, mod)) % mod) % mod
print(s % mod)
