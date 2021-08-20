N = int(input())
V = 0
E = 0
for _ in range(N - 1):
    (u, v) = map(int, input().split())
    if v < u:
        (u, v) = (v, u)
    E += u * (N - v + 1)
for i in range(1, N + 1):
    V += i * (N + 1 - i)
print(V - E)
