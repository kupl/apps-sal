for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    hsh=[0]*max(a)
    for i in a:
        hsh[i-1]+=1
    flag=0
    for i in hsh:
        flag+=i%2
        if(flag):
            break
    if(flag):
        print("NO")
    else:
        a.sort()
        s=a[0]*a[-1]
        for i in range(2*n):
            if(a[i]*a[4*n-1-i]!=s):
                flag=1
                break
        if(flag):
            print("NO")
        else:
            print("YES")


