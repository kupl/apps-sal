n = int(input())
l = []
for x in range(n):
    m = input().split()
    a = (int(m[0]), int(m[1]))
    l.append(a)
l = sorted(l)
h = 0
for x in range(n - 1):
    if l[x][0] < l[x + 1][0] and l[x][1] > l[x + 1][1]:
        h = 1
if h == 1:
    print('Happy Alex')
else:
    print('Poor Alex')
