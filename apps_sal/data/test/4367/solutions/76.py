(N, R) = map(int, input().split())
print((R, R + 100 * (10 - N))[N <= 10])
