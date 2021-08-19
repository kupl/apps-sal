(*l,) = sorted(list(map(int, input().split())))
if l[0] + l[-1] == l[1] + l[2] or sum(l[:3]) == l[3]:
    print('YES')
else:
    print('NO')
