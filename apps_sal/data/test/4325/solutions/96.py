N, X, T = map(int, input().split())

if N % X == 0:
    print((N//X)*T)
else:
    N = N //X + 1
    print(N*T)
