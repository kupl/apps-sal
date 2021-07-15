import sys
q=int(input())
for i in range(q):
    n=int(sys.stdin.readline())
    a=[int(i) for i in sys.stdin.readline().split()]
    minrazn=999999
    a.sort()
    ch=0
    nch=0
    for k in range(n):
        if k<n-1:
            if a[k]%2==0:
                ch+=1
            else:
                nch+=1
            if minrazn>a[k+1]-a[k] and a[k+1]!=a[k] :
                minrazn=a[k+1]-a[k]
        else:
            if a[k]%2==0:
                ch+=1
            else:
                nch+=1
    if ch%2==0:
        print('YES')
    elif minrazn==1:
        print('YES')
    else:
        print('NO')
        

