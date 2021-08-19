(N, K, M) = map(int, input().split())
A = list(map(int, input().split()))
worst_score = sum(A)
score = N * M - worst_score
if score <= K:
    if score > 0:
        print(score)
    else:
        print(0)
else:
    print(-1)
