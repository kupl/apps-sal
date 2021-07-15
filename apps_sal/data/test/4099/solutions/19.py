#151b
#1.値を受け取る
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

#2.残りのテストで何点取れは大丈夫か判断する。
answer = (N * M) - sum(A)

if answer <= K:
    if answer < 0:
        print('0')
    else:
        print(answer)
else:
    print('-1')
