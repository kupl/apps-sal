n=int(input())
for i in range(n):
    a,b=[int(x) for x in input().split(' ')]
    if (a+b) % 3 != 0:
        print('NO')
    else:
        if max(a,b)>2*min(a,b):
            print('NO')
        else:
            if (2*min(a,b)-max(a,b)) % 3 == 0:
                print('YES')
            else:
                print('NO')

