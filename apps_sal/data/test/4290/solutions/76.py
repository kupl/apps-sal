N, M = map(int, input().split())
x = N + M
print(x * (x - 1) // 2 - N * M)
