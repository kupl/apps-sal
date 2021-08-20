from heapq import *
(X, Y, Z, K) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A = sorted(A, reverse=True)
B = sorted(B, reverse=True)
C = sorted(C, reverse=True)
cake = []
heapify(cake)
for x in range(X):
    for y in range(min(Y, K // (x + 1) + 1)):
        for k in range(min(Z, K // ((x + 1) * (y + 1)) + 1)):
            heappush(cake, -(A[x] + B[y] + C[k]))
for _ in range(K):
    print(abs(heappop(cake)))
