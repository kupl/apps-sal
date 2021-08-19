n = int(input())
h = [False for i in range(n)]
v = [False for i in range(n)]
z = []
for i in range(n * n):
    (a, b) = list(map(int, input().split()))
    a -= 1
    b -= 1
    if not h[a] and (not v[b]):
        z.append(i + 1)
        h[a] = True
        v[b] = True
print(*z)
