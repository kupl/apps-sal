(K, N) = map(int, input().split())
A = list(map(int, input().split()))
d = []
for i in range(N - 1):
    d.append(A[i + 1] - A[i])
d.append(A[0] + K - A[N - 1])
max_d = max(d)
print(K - max_d)
