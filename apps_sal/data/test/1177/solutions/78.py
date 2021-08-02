from numpy import*
(n, s), a, m, e = map(int, input().split()), list(map(int, input().split())), 998244353, 3001; D = zeros((n, e)); D[0][a[0]] = 1
for j, i in enumerate(a[1:]): D[j + 1, i] += j + 2; D[j + 1, i:] += D[j, :e - i]; D[j + 1, :] = (D[j + 1, :] + D[j, :]) % m
print(int(sum(D[:, s]) % m))
