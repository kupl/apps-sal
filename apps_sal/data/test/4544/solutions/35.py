from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))

d = defaultdict(int)

for x in arr:
    d[x] += 1
    d[x - 1] += 1
    d[x + 1] += 1

result = [y for x, y in d.items()]

print(max(result))
