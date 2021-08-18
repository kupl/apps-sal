N, K, M = map(int, input().split())
A = list(map(int, input().split()))

answer = (N * M) - sum(A)

if answer <= K:
    if answer < 0:
        print('0')
    else:
        print(answer)
else:
    print('-1')
