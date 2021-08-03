import sys
t, k = (int(x) for x in sys.stdin.readline().split())
mod = 1000000007
l = [0] * 100001
l[0] = 1
for i in range(1, 100001):
    l[i] = (l[i - 1] + (l[i - k] if i - k >= 0 else 0)) % mod
for i in range(1, 100001):
    l[i] = (l[i] + l[i - 1]) % mod
for i in range(t):
    a, b = (int(x) for x in sys.stdin.readline().split())
    print((l[b] - l[a - 1] + mod) % mod)
