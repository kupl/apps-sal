N, K = map(int, input().split())
result = 1
while N >= K:
    N = int(N / K)
    result += 1
print(result)
