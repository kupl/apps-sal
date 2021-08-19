(N, M) = map(int, input().split())
S = set([x for x in range(1, M + 1)])
for i in range(N):
    A = list(map(int, input().split()))
    B = set(A[1:])
    S = S & B
print(len(S))
