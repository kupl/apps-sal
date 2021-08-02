import sys
n = int(input())
l = []

for i in range(n):
    a, b = map(int, input().split())
    l.append([a, b])

l = sorted(l, key=lambda x: (x[1]))

c = 0
for i in range(n):
    c += l[i][0]
    if c > l[i][1]:
        print('No')
        return
    else:
        continue

print('Yes')
