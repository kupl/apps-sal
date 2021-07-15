import heapq

N = int(input())
A = list(map(int, input().split()))

L = A[:N]
heapq.heapify(L)
Lmax = [0] * (N + 1)
Lsum = sum(L)
Lmax[0] = Lsum
for i in range(N, 2 * N):
    m = heapq.heappushpop(L, A[i])
    Lsum += A[i] - m
    Lmax[i - N + 1] = Lsum

R = [-x for x in A[2 * N:]]
heapq.heapify(R)
Rmin = [0] * (N + 1)
Rsum = -sum(R)
Rmin[N] = Rsum
for i in range(2 * N - 1, N - 1, -1):
    M = -heapq.heappushpop(R, -A[i])
    Rsum -= M - A[i]
    Rmin[i - N] = Rsum

print((max(Lmax[i] - Rmin[i] for i in range(N + 1))))

