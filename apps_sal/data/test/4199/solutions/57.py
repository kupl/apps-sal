N, K = map(int, input().split())
heights = list(map(int, input().split()))

result = 0

for h in heights:
    if h >= K:
        result += 1
print(result)
