import sys

n = int(input())
a = [int(x) for x in input().split()]
d = {}
for x in a:
    c = d.get(x, 0) + 1
    if c == 3:
        print('NO')
        return
    d[x] = c

r1 = []
r2 = []
for key, value in d.items():
    r1.append(key)
    if value > 1: r2.append(key)

r1.sort()
r2.sort(reverse=True)

print('YES')
print(len(r1))
for x in r1:
    print(x, end=' ')
print()
print(len(r2))
for x in r2:
    print(x, end=' ')
