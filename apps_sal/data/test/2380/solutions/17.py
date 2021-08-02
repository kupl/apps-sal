import bisect
import heapq
N, M = map(int, input().split())
A = list(map(int, input().split()))
heapq.heapify(A)
BC = []
for i in range(M):
    B, C = map(int, input().split())
    BC.append((B, C))
BC.sort(key=lambda x: x[1], reverse=True)
A.sort()
now = 0
D = [0] * N
for i in range(M):
    B = BC[i][0]
    C = BC[i][1]
    for j in range(now, min(now + B, N)):
        D[j] = C
    now += B
    if now > N - 1:
        break

for i in range(N):
    a = A[i]
    d = D[i]
    if d > a:
        A[i] = d
    else:
        break
print(sum(A))
