(N, K) = map(int, input().split())
H = []
sa = []
for i in range(N):
    H.append(int(input()))
H.sort()
for j in range(N - K + 1):
    sa.append(H[K + j - 1] - H[j])
print(min(sa))
