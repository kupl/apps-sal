l = [int(x) for x in input().split()]
l.sort()
if l[0] + l[3] == l[1] + l[2] or l[0] + l[1] + l[2] == l[3] or l[0] + l[1] == l[2] + l[3] or (l[0] == l[1] + l[2] + l[3]) or (l[0] + l[2] == l[1] + l[3]):
    print('YES')
else:
    print('NO')
