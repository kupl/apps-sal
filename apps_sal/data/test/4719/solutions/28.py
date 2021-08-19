import collections as c
n = [c.Counter(input()) for _ in range(int(input()))]
r = n[0]
for i in range(1, len(n)):
    r = r & n[i]
print(*sorted([i * j for (i, j) in r.items()]), sep='')
