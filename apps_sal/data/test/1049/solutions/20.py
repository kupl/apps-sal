n, d = list(map(int, input().split()))
best, cur = 0, 0
for i in range(d):
    day = list(set(input()))
    if day != ['1']:
        cur += 1
    else:
        cur = 0
    best = max(best, cur)
print(best)
