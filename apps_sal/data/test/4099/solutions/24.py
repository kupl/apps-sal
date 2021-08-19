(N, K, M) = map(int, input().split())
scores = list(map(int, input().split()))
answer = max(M * N - sum(scores), 0)
if answer <= K:
    print(answer)
else:
    print('-1')
