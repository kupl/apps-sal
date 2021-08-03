f = []
f.append(1)
f.append(1)
mod = 1e9 + 7
for i in range(100010):
    f.append((f[-1] + f[-2]) % mod)
n, m = list(map(int, input().split()))
print(int(2 * (f[n] + f[m] - 1) % mod))
