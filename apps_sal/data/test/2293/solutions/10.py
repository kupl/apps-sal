import math
(m, n) = list(map(int, input().split()))
days = []
for z in range(m):
    t = set(list(map(int, input().split()))[1:])
    days.append(t)
check = True
for i in range(m):
    for j in range(i):
        if not days[i].intersection(days[j]):
            check = False
            break
        if not check:
            break
if check:
    print('possible')
else:
    print('impossible')
