N, K, X, Y = [int(input()) for _ in range(4)]
result = min(N, K)
N -= result
result *= X

if N >= 0:
    result += N * Y
print(result)
