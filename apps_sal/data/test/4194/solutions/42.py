# ABC163
N, M = map(int, input().split())
A = []
A = [int(M) for M in input().split()]
if N - sum(A) >= 0:
    print(N - sum(A))
else:
    print(-1)
