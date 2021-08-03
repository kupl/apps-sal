N, M = map(int, input().rstrip().split(" "))
k = N * 2 + M
print(min(k // 4, M // 2))
