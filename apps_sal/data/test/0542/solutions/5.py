__author__ = 'PrimuS'

n = int(input())
p1 = [0] * n
p2 = [0] * n
n1 = 0
n2 = 0
last = -1

for i in range(n):
    a = int(input())
    if a > 0:
        p1[n1] = a
        n1 += 1
        last = 1
    else:
        p2[n2] = -a
        n2 += 1
        last = 2

s1 = sum(p1)
s2 = sum(p2)

if s1 > s2:
    print('first')
elif s2 > s1:
    print('second')
else:
    res = 0
    i = 0
    while i < len(p1) and i < len(p2):
        if p1[i] > p2[i]:
            res = 1
        elif p2[i] > p1[i]:
            res = 2
        i += 1
        if res != 0:
            break
    if res > 0 or (res == 0 and len(p1) != len(p2)):
        if res == 1 or (res == 0 and len(p1) > len(p2)):
            print('first')
        else:
            print('second')
    else:
        if last == 1:
            print('first')
        else:
            print('second')
