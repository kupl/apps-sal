def check(start):
    nonlocal groups
    cnt = 2
    d = 1
    while d <= min(start, len(groups) - start - 1):
        if groups[start - d][0] == groups[start + d][0]:
            if groups[start - d][1] + groups[start + d][1] >= 3:
                cnt += groups[start - d][1] + groups[start + d][1]
                d += 1
                continue
        return cnt
    return cnt

n, k, x = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
groups = []
i = 0
while i < n - 1:
    if c[i] == c[i + 1]:
        groups.append([c[i], 2])
        i += 2
    else:
        groups.append([c[i], 1])
        i += 1
if n == 1 or c[-1] != c[-2]:
    groups.append([c[-1], 1])
res = 0
for i in range(len(groups)):
    if groups[i][0] == x and groups[i][1] == 2:
        res = max(res, check(i))
print(res)
