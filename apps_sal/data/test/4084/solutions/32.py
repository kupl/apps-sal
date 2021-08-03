N, A, B = map(int, input().split())
D, M = divmod(N, A + B)
print((D * A) + min(M, A))
