a = input()
flag = 0
if len(a) % 2 == 1:
    q = len(a) // 2
    w = q
else:
    q = len(a) // 2 - 1
    w = len(a) // 2
while(q > 0 and flag == 0):
    if(a[:w + 1] == a[q:]):
        s = a[:w + 1]
        flag = 1
    else:
        q -= 1
        w += 1
if flag:
    print('YES')
    print(s)
else:
    print('NO')
