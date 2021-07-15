N, X, T = list(map(int, input().split()))
s = N // X

if N % X == 0:
    print((s*T))
else:
    print(((s+1)*T))

