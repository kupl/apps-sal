import sys

s = input().split()
r,c = list(map(int, s))
f = ['']*r
for x in range(r):
    f[x] = input().replace('.', 'D')
    if 'WS' in f[x] or 'SW' in f[x]:
        print('No')
        return
    if x > 0:
        for y in range(c):
            up = f[x][y]+f[x-1][y]
            if up in ['SW', 'WS']:
                print('No')
                return
print('Yes')
for x in range(r):
    print(f[x])

