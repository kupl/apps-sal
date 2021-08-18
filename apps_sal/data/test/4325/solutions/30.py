N, X, T = list(map(int, input().split()))
if N % X == 0:
    answer = (N / X * T)
else:
    answer = (N // X + 1) * T
print((int(answer)))
