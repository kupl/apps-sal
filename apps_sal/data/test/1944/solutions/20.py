n = int(input())
m = list()
for i in range(n):
    m.append(list((int(x) for x in input().split())))
m.sort()
ok = 1
for i in range(n - 1):
    if m[i][1] > m[i + 1][1]:
        print('Happy Alex')
        ok = 0
        break
if ok == 1:
    print('Poor Alex')
