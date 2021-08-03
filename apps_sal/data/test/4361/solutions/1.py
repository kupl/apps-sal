N, K = map(int, input().split())
L = []
for i in range(N):
    L.append(int(input().rstrip()))
L.sort()
M = []
for i in range(N - K + 1):
    M.append(L[K + i - 1] - L[i])
M.sort()
print(M[0])
