for _ in range(int(input())):
    l = list(input())
    l.sort()
    l = "".join(l)
    x = len(l)
    s = input()
    n = len(s)
    flag = False
    for i in range(n):
        m = list(s[i:i + x])
        m.sort()
        m = ''.join(m)
        if(m == l):
            flag = True
            break
    if(flag):
        print("YES")
    else:
        print('NO')
