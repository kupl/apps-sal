N = int(input())
K = int(input())
X = int(input())
Y = int(input())
if K < N:
    print(K * X + (N - K) * Y)
else:
    print(N * X)
