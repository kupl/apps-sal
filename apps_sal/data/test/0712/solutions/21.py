(n, p, t) = input().split()
(n, p) = (int(n), float(p))
f = [p] * n + [0]
for i in range(int(t) - 1):
    f = [f[k] * (1 - p) + p * (1 + f[k - 1]) for k in range(n)] + [0]
print(f[-2])
