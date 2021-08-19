# coding gbk
#!usr/bin/env
n = int(input())
a = [0] + [n for i in range(n)]
e = [[i + 1, i - 1] if i < n else [i - 1] for i in range(0, n + 1)]
e[0] = []
a[1] = 0
for i, x in enumerate(map(int, input().split())):
    if i + 1 != x:
        e[i + 1] += [x]
q = [(0, 1)]
while q:
    l, cur = q.pop(0)
    for x in e[cur]:
        if l + 1 < a[x]:
            a[x] = l + 1
            q.append((l + 1, x))
print(*a[1:])
