N, K, M = map(int, input().split())
A = list(map(int, input().split()))

need_score = N * M - sum(A)

if K >= need_score:
    if need_score <= 0:
        print(0)
    else:
        print(need_score)
else:
    print(-1)
