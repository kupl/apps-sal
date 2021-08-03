N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Asum = [0]
Bsum = [0]

for i in range(N):
    Asum.append(Asum[-1] + A[i])

for i in range(M):
    Bsum.append(Bsum[-1] + B[i])

m = 0
j = M

for i in range(len(Asum)):
    if Asum[i] > K:
        break
    while Asum[i] + Bsum[j] > K:
        j -= 1
    if m < i + j:
        m = i + j

print(m)
