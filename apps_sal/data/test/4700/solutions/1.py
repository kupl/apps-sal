N, M = list(map(int, input().split()))
H = [int(a) for a in input().split()]
X = [1] * N
for _ in range(M):
    a, b = list(map(int, input().split()))
    a, b = a-1, b-1
    if H[a] <= H[b]:
        X[a] = 0
    if H[b] <= H[a]:
        X[b] = 0
print((sum(X)))

