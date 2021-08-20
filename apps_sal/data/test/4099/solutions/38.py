(N, K, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
X = M * N - sum(A)
if X > K:
    print('-1')
elif 0 <= X <= K:
    print(X)
else:
    print('0')
