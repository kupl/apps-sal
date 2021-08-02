N, K = map(int, input().split())
result = 0
for i in range(1, N + 1):
    prob = 1
    count = i
    while count < K:
        prob *= 0.5
        count *= 2
    result += prob / N
print(result)
