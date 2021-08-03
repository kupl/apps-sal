a, b = map(int, input().split())
flag = True
for i in range(1, 1000000):
    if(flag == True):
        flag = False
        if(a < i):
            print('Vladik')
            return
        a -= i
    else:
        flag = True
        if(b < i):
            print('Valera')
            return
        b -= i
