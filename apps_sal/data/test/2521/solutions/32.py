from heapq import heapify, heappushpop
(N, *A) = map(int, open(0).read().split())
(L, C, R) = (A[:N], A[N:2 * N], A[2 * N:])
F = [sum(L)]
heapify(L)
for c in C:
    F.append(F[-1] + c - heappushpop(L, c))
R = [-r for r in R]
B = [sum(R)]
heapify(R)
for c in reversed(C):
    B.append(B[-1] - c - heappushpop(R, -c))
print(max((f + b for (f, b) in zip(F, reversed(B)))))
