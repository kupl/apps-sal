t = list(map(int, input().split()))
best = sum(t)
for x in t:
    if t.count(x) == 1:
        continue
    best = min(best, sum(t) - x * min(3, t.count(x)))
print(best)
