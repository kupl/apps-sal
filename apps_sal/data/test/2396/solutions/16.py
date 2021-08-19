import re
m = int(input())
lis = list()
for i in range(m):
    s = input()
    lis += [re.split('\\W+', s)]
d = dict()
for i in range(m):
    ans = int(lis[i][1]) + int(lis[i][2])
    ans = ans / int(lis[i][3])
    lis[i][0] = ans
    if ans in d:
        d[ans] += 1
    else:
        d[ans] = 1
for i in range(m):
    print(d[lis[i][0]], end=' ')
