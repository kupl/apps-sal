N, K = list(map(int, input().split()))
A = [int(a) for a in input().split()]
D = sorted([A[i + 1] - A[i] for i in range(N - 1)])
print(A[-1] - A[0] - (sum(D[-K + 1:]) if K - 1 else 0))
