n = int(input())
E = 0
V = 0
for i in range(n - 1):
    (u, v) = list(map(int, input().split()))
    u -= 1
    v -= 1
    if u > v:
        (u, v) = (v, u)
    E += (u + 1) * (n - v)
for i in range(n):
    V += n + i * n - i - i * i
print(V - E)
