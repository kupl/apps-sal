from collections import Counter
n, m = list(map(int, input().split()))

b = Counter(list(map(int, input().split())))


res = 0
for days in range(1, m // n + 1):
    parts = 0
    for j in list(b.values()):
        parts += j // days
    if parts >= n:
        res = days

print(res)
