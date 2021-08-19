mod = 10 ** 9 + 7
MAX = 2 * 10 ** 5 + 10
r = [1] * MAX
f = [1] * MAX
rf = [1] * MAX
rp2 = [1] * MAX
for i in range(2, MAX):
    f[i] = f[i - 1] * i % mod
    r[i] = mod - mod // i * r[mod % i] % mod
    rf[i] = rf[i - 1] * r[i] % mod
for i in range(1, MAX):
    rp2[i] = rp2[i - 1] * (mod + 1) // 2 % mod
(n, T) = list(map(int, input().split()))
t = list(map(int, input().split()))
t.append(10 ** 14 + 1)
S = 0
E = 0
for i in range(len(t)):
    cof = rp2[1]
    for add in range(2):
        (l_, r_) = (max(0, T - S - (t[i] - add)), min(i, T - S))
        for x in range(l_, r_ + 1):
            E = (E + i * (f[i] * rf[x] * rf[i - x]) * rp2[i] * cof) % mod
    S += t[i]
print(E)
