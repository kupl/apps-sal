(n, k, d) = list(map(int, input().split()))
f = [0] * (n + k + 1)
f_ = [0] * (n + k + 1)
f_[0] = 1
for i in range(1, n + 1):
    for j in range(1, k + 1):
        f[i] += f[i - j]
    for j in range(d, k + 1):
        f[i] += f_[i - j]
    for j in range(1, d):
        f_[i] += f_[i - j]
print(f[n] % (10 ** 9 + 7))
