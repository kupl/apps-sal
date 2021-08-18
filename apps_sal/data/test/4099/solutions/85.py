

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

if 0 <= (N * M) - sum(A) <= K:
    print((N * M) - sum(A))

elif K < (N * M) - sum(A):
    print(-1)

else:
    print(0)
