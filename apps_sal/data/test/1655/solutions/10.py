n = int(input())
lengths = list(map(int, input().split()))
limit = n - 1
result = 1
for i in range(len(lengths) - 1, -1, -1):
    if limit > i:
        result += 1
    if limit > i - lengths[i]:
        limit = i - lengths[i]
print(result)
