(N, K, M) = map(int, input().split())
scores = list(map(int, input().split()))
achieve_score = N * M
answer = achieve_score - sum(scores)
if answer <= 0:
    print(0)
elif answer <= K:
    print(answer)
else:
    print('-1')
