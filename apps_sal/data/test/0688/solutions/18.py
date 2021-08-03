from collections import defaultdict
ag = defaultdict(int)
for i in input():
    if i == '9':
        ag['6'] += 1
    elif i == '5':
        ag['2'] += 1
    else:
        ag[i] += 1
g = defaultdict(int)
for i in input():
    if i == '9':
        g['6'] += 1
    elif i == '5':
        g['2'] += 1
    else:
        g[i] += 1
ans = 999999999999999999
for i in ag:
    ans = min(ans, g[i] // ag[i])
print(ans)
