(k, a, b) = map(int, input().split())
m = 1000000007
d = a * pow(b, m - 2, m) % m
c = pow(a + b, m - 2, m)
(u, v) = ([0] * k, [0] * k)
for s in range(k, 0, -1):
    v[s - 1] = s + d
    for i in range(s, k):
        j = max(i - s, s - 1)
        v[i] = c * (a * u[i] + b * (s + v[j])) % m
    (u, v) = (v, u)
print(u[k - 1])
