(K, N) = map(int, input().split())
A = list(map(int, input().split()))
d = [K + A[0] - A[-1]] + [b - a for (a, b) in zip(A, A[1:])]
print(K - max(d))
