n = int(input())
a = list(map(int, input().split()))
k1 = a[0]
s1 = a[1:]
a = list(map(int, input().split()))
k2 = a[0]
s2 = a[1:]
flag = 0
fights = 0
count = 0
while len(s1) != 0 and len(s2) != 0:
    count += 1
    if count > 1000000:
        flag = 1
        break
    t = s1.pop(0)
    p = s2.pop(0)
    if t > p:
        s1.append(p)
        s1.append(t)
    else:
        s2.append(t)
        s2.append(p)
    fights += 1
if flag == 1:
    print('-1')
else:
    if len(s1) == 0:
        won = '2'
    else:
        won = '1'
    print(fights, won, sep=' ')
