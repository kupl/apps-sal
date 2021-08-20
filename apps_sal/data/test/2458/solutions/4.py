(t, k) = list(map(int, input().split()))
MAXA = 10 ** 5 + 1
mod = 10 ** 9 + 7
f = [0] * MAXA
s = [0] * MAXA
for i in range(k):
    f[i] = 1
for i in range(k, MAXA):
    f[i] = (f[i - 1] + f[i - k]) % mod
for i in range(1, MAXA):
    s[i] = (s[i - 1] + f[i]) % mod
for i in range(t):
    (a, b) = list(map(int, input().split()))
    result = (s[b] - s[a - 1] + mod) % mod
    print(result)
