(N, X, T) = map(int, input().split())
A = N // X + 1
if N % X == 0:
    A -= 1
print(A * T)
