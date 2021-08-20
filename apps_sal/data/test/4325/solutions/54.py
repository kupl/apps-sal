(N, X, T) = map(int, input().split())
W = N // X
M = N % X
if M == 0:
    print(W * T)
else:
    print(T * (W + 1))
