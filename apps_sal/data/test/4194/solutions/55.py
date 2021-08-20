(N, M) = map(int, input().split())
A = list(map(int, input().split()))
if N - sum(A) >= 0:
    print(N - sum(A))
else:
    print(-1)
