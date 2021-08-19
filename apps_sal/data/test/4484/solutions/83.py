(n, m) = list(map(int, input().split()))
f = [1]
p = 10 ** 9 + 7
for i in range(1, max(n, m) + 1):
    f.append(f[-1] * i % p)
if abs(n - m) == 1:
    print(f[n] * f[m] % p)
elif abs(n - m) == 0:
    print(f[n] * f[m] * 2 % p)
else:
    print(0)
