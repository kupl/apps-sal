(N, X, T) = map(int, input().split())
print(T * (N // X) + T if N % X != 0 else T * (N // X))
