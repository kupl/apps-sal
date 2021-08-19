import re
s = input()
l = re.compile('[|]+').findall(s)
diff = len(l[0]) + len(l[1]) - len(l[2])
if diff == 0:
    print(s)
elif diff == -2:
    print(l[0] + '|+' + l[1] + '=' + l[2][:-1])
elif diff == 2:
    l[2] += '|'
    if len(l[0]) == 1:
        l[1] = l[1][:-1]
    else:
        l[0] = l[0][:-1]
    print(l[0] + '+' + l[1] + '=' + l[2])
else:
    print('Impossible')
