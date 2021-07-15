n = int(input())
names = []
for i in range(n):
    names.append(input().split())
p = [int(i) - 1 for i in input().split()]
last = min(names[p[0]][0], names[p[0]][1])
for i in range(1, n):
    a = names[p[i]]
    v = []
    if last < a[0] :
        v.append(a[0])
    if last < a[1]:
        v.append(a[1])
    if len(v) == 0:
        print('NO')
        break
    else:
        last = min(v)
else:
    print('YES')

