K, N = list(map(int, input().split()))
A = list(map(int, input().split()))

A2 = [K+a for a in A]
A3 = A + A2

dist = [0] * N
for i in range(N):
    j = i + N - 1
    dist[i] = A3[j] - A[i]

print((min(dist)))


