(N, K, M) = map(int, input().split())
score = list(map(int, input().split()))
lastscore = N * M - sum(score)
if lastscore <= 0:
    print('0')
elif K >= lastscore:
    print(lastscore)
else:
    print('-1')
