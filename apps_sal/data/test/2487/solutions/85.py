n = int(input())
a = sum(-~i * (n - i) for i in range(n))
for _ in range(n - 1):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    a -= u * (n - v + 1)
print(a)
