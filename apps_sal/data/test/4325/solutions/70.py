(N, X, T) = map(int, input().split())
if N % X == 0:
    count = N // X
else:
    count = N // X + 1
print(count * T)
