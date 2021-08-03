from sys import stdin

input = stdin.readline

mod = 998244353

inv = [0] * 103
inv[1] = 1
for i in range(2, 101):
    inv[i] = (mod - mod // i) * inv[mod % i] % mod

n = int(input())

h = [0] * (n + 3)
h[0] = 1
for i in range(1, n + 2):
    h[i] = h[i - 1] * 100 % mod


p = list(map(int, input().split()))
tot = 1 * h[n] % mod
now = 1
iv = 1
for i in range(n):
    if i == n - 1:
        iv = iv * inv[p[i]] % mod
        continue
    now = now * p[i] % mod
    tot += now * h[n - i - 1] % mod
    tot %= mod
    iv = iv * inv[p[i]] % mod

print(tot * iv % mod)
