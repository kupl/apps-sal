a =input()
if len(a) % 2 == 1:
    i1 = len(a)// 2
    s1 = a[i1]
    for i in range(1, i1 + 1):
        s1 += a[i1 + i]
        s1 += a[i1 - i]
    print(s1)
    
else:
    a1 = ' ' + a
    i1 = len(a)// 2
    s1 = a1[i1]
    for i in range(1, i1 + 1):
        s1 += a1[i1 + i]
        s1 += a1[i1 - i]
    
    print(s1[:-1])

