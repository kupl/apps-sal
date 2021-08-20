import itertools
(n, m) = list(map(int, input().split(' ')))
l = [[] for i in range(n + 1)]
for i in range(m):
    (a, b) = list(map(int, input().split(' ')))
    l[a].append(b)
    l[b].append(a)
result = 0
sum = 4000
for i in range(n):
    lis = []
    for s in l[i]:
        if s > i:
            lis.append(s)
    for enum in itertools.combinations(lis, 2):
        (x, y) = enum
        temp = len(l[i]) + len(l[x]) + len(l[y]) - 6
        if temp < sum and x in l[y]:
            sum = temp
if sum == 4000:
    result = -1
else:
    result = sum
print(result)
