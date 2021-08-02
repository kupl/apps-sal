N, X, Y = [int(_) for _ in input().split()]
X -= 1
Y -= 1

V = [0 for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        v1 = j - i
        v2 = abs(i - X) + abs(j - Y) + 1
        V[min(v1, v2)] += 1

for v in V[1:]:
    print(v)
