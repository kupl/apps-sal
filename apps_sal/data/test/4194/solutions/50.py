N, M = map(int, input().split())
A = map(int, input().split())
AA = sum(A)

if N >= AA:
    print(N - AA)
else:
    print(-1)
