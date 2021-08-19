(n, a, b, k) = list(map(int, input().split()))
s = input()
m = int(1000000000.0 + 9)
a_1 = pow(a, m - 2, m)
x = a_1 * b % m
xk = pow(x, k, m)
C = 0
for i in range(0, k):
    z = 1 if s[i] == '+' else -1
    C = (C + z * pow(x, i, m)) % m
kk = (n + 1) // k
if xk > 1:
    v1 = (pow(xk, kk, m) - 1) % m
    v2 = pow((xk - 1) % m, m - 2, m)
    D = v1 * v2 % m
else:
    D = kk
ans = pow(a, n, m) * C * D
ans %= m
print(ans)
