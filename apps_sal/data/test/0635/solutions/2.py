n,s=map(int,input().split())
a=[int(s) for s in input().split()]
b=[int(s) for s in input().split()]
if a[0]==0:
    print('NO')
else:
    if a[s-1]==1:
        print('YES')
    else:
        if b[s-1]==0:
            print('NO')
        else:
            for i in range(s,n):
                if a[i]==1 and b[i]==1:
                    print('YES')
                    break
            else:
                print('NO')
