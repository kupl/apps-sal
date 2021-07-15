for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    t=[]
    k=0
    for i in range(0,2*n,2):
        if a[i]==a[i+1] and a[4*n-i-1]==a[4*n-i-2]:
            s=a[i]*a[4*n-i-1]
            t.append(s)
            

        else:
            k+=1
    if k>0:
        print('NO')
    else:
        if len(list(set(t)))==1:
            print('YES')
        else:
            print('NO')

