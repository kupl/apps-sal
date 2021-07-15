n = int(input())
l = list(map(int, input().split()))
s = set()
for i in l:
    s.add(i)
l = list(s)
l.sort()
if len(l) > 3:
    print('NO')
if len(l) == 3:
    if (l[0] + l[2]) / 2 == l[1]:
        print('YES')
    else:
        print('NO')
if len(l) <= 2:
    print('YES')
