N, K, M = list(map(int, input().split()))
score = list(map(int, input().split()))

sum_score = sum(score)
answer = N * M - sum_score

if answer > K:
    print('-1')

elif answer <= 0:
    print('0')

else:
    print(answer)
