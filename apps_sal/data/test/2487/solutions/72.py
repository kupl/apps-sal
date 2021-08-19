import sys
N = int(sys.stdin.readline().rstrip())

V = 0
for i in range(N):
    V += (N - i) * (i + 1)

E = 0
for _ in range(N - 1):
    u, v = list(map(int, sys.stdin.readline().rstrip().split()))
    if u > v:
        u, v = v, u
    E += u * (N - v + 1)

# print(V,E)
print((V - E))
