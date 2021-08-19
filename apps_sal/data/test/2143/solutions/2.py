from collections import defaultdict
n = int(input())
a = sorted(list(map(int, input().split())))
count = defaultdict(int)
for (i, x) in enumerate(a[:-1]):
    for (j, y) in enumerate(a[i + 1:]):
        count[x + y] += 1
print(max(count.values()))
