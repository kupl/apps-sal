K, N = list(map(int, input().split()))
A = list(map(int, input().split()))

A3 = A + [K + a for a in A]
dist = [A3[i + N - 1] - A[i] for i in range(N)]

print((min(dist)))
