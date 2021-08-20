(N, K, M) = map(int, input().split())
A = map(int, input().split())
score = M * N - sum(A)
if score <= 0:
    print(0)
elif score <= K:
    print(score)
else:
    print('-1')
