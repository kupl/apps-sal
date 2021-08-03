K, N = map(int, input().split())
A = list(map(int, input().split()))
sa = []

for i in range(N - 1):
    sa.append(A[i + 1] - A[i])

sa.append((A[0] - A[N - 1]) % K)

print(K - max(sa))
