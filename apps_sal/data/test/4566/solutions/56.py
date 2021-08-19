(N, M) = map(int, input().split())
L = [0] * N
for i in range(M):
    (a, b) = map(int, input().split())
    L[a - 1] += 1
    L[b - 1] += 1
print(*L, sep='\n')
