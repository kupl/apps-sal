n, k = map(int, input().split())
m = 10**9 + 7
l = [0] * (k + 1)
a = 0
for i in range(k, 0, -1):
    l[i] = pow(k // i, n, m)
    for j in range(2, k // i + 1):
        l[i] -= l[i * j]
    a += i * l[i]
    a %= m
print(a)
