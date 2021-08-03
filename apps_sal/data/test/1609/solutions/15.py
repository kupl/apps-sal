n = int(input())

a = [int(i) for i in input().split(' ')]

m = {}

for i in range(1, 100001):
    m[i] = []

zeroIndexes = []

for i in range(n):
    m[a[i]].append(i)

for i in range(1, n + 1):
    if len(m[i]) == 0:
        zeroIndexes.append(i)

for i in range(1, 100001):
    if len(m[i]) == 0:
        continue
    mx = 1 if i <= n else 0
    while len(m[i]) > mx:
        a[m[i][-1]] = zeroIndexes[-1]
        m[i].pop()
        zeroIndexes.pop()

print(' '.join([str(s) for s in a]))
