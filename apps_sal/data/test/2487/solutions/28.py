N = int(input())
edge = 0
for i in range(N - 1):
    (u, v) = map(int, input().split())
    if u > v:
        a = u
        u = v
        v = a
    edge += u * (N - v + 1)
vertice = 0
for i in range(1, N + 1):
    vertice += i * (N - i + 1)
print(vertice - edge)
