# coding: utf-8
n, m = [int(i) for i in input().split()]
if not m:
    print('YES')
    return
d = [int(i) for i in input().split()]
if n in d or 1 in d:
    print('NO')
    return
d.sort()
i = 0
while i < m - 2:
    if d[i + 2] - d[i + 1] == 1:
        if d[i + 1] - d[i] == 1:
            print('NO')
            break
        else:
            i += 1
    else:
        i += 2
else:
    print('YES')
