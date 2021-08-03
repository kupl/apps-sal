N, M, *A = map(int, open(0).read().split())
print(max(-1, N - sum(A)))
