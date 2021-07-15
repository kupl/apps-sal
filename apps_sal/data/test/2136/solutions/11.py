for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        s=input()
        t=[]
        for j in s:
            t.append(j)
        a.append(t)
    if a[0][1]==a[1][0]:
        if a[n-1][n-2]==a[n-2][n-1]:
            if a[n-1][n-2]==a[0][1]:
                print(2)
                print(n,n-1)
                print(n-1,n)
            else:
                print(0)
        else:
            if a[n-1][n-2]==a[0][1]:
                print(1)
                print(n,n-1)
            else:
                print(1)
                print(n-1,n)
    else:
        if a[n-1][n-2]==a[n-2][n-1]:
            if a[n-1][n-2]==a[0][1]:
                print(1)
                print(1,2)
            else:
                print(1)
                print(2,1)
        else:
            print(2)
            if a[0][1]=='0':
                print(2,1)
            else:
                print(1,2)
            if a[n-1][n-2]=='1':
                print(n-1,n)
            else:
                print(n,n-1)

