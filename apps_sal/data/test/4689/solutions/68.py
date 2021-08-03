K, N = map(int, input().split())
A = list(map(int, input().split()))

T = []

for i in range(1, N):
    T.append(A[i] - A[i - 1])

T.append(K - A[N - 1] + A[0])

print(sum(T) - max(T))
