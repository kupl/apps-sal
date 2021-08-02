n = int(input())

V = 0
for i in range(1, n + 1):
    V += i * (n - (i - 1))

E = 0
for _ in range(n - 1):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    E += u * (n - (v - 1))

print(V - E)
