N, X, T = map(int, input().split())
a, b = N // X, N % X
if b:
    print((a + 1) * T)
else:
    print(a * T)
