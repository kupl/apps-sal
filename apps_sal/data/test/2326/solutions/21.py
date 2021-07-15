m = 998244353
n = int(input())
u = [1] + [0] * n
for a in map(int, input().split()):
    v = u[:]
    if 0 < a < n: v[a] += u[0]
    for j in range(n): v[j] = (v[j] + u[j + 1]) % m
    u = v
print((u[0] - 1) % m)
r= 6

