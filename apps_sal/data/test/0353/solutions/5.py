arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

n = int(input())
prr = [int(x) for x in input().split()]
if(n==1):
    a = prr[0]
    if(a==0):
        print('UP')
    elif(a==15):
        print('DOWN')
    else:
        print(-1)
else:
    a,b = prr[n-2],prr[n-1]
    c = b-a
    if(c==1):
        if(b!=15):
            print('UP')
        else:
            print('DOWN')
    else:
        if(b!=0):
            print('DOWN')
        else:
            print('UP')
