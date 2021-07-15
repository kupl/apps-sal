from collections import defaultdict

n = int(input())

a = list(map(int, input().split()))

counts = defaultdict(int)

for x in a:
    counts[x] += 1

keys = set()
c = len(counts)
ans = 0

for x in a[:-1]:
    if x not in keys:
        keys.add(x)
        counts[x] -= 1
        if counts[x] == 0:
            c -= 1
        ans += c
    else:
        counts[x] -= 1
        if counts[x] == 0:
            c -= 1
print(ans)
