a, b = input(), input()
if len(a) != len(b): print('NO')
else:
    u, v = 0, 0
    for i in a: 
        if i == '1':
            u = 1
            break
    for i in b: 
        if i == '1':
            v = 1
            break                 
    if u == v: print('YES')
    else: print('NO')
