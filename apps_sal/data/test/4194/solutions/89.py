N, M, *A = map(int, open(0).read().split())
print([s := N - sum(A), -1][s < 0])
