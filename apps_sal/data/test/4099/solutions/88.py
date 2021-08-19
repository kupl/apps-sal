(N, K, M) = map(int, input().split())
scores = list(map(int, input().split()))
x = M * N - sum(scores)
if x > K:
    print('-1')
elif 0 < x:
    print(x)
else:
    print('0')
