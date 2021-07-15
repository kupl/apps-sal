s=input()
a,b,c='(',')','#'
s1=len(s)
a1,b1,c1,r=0,0,0,1
if(s[-1]==a):
    print(-1)
else:
    for i in range(s1):
        if(s[i]==a):
            a1+=1
        if(s[i]==b):
            b1+=1
        if(s[i]==c):
            c1+=1
        if(b1+c1>a1):
            r=0
            break
    if(r==0):
        print(-1)
    else:
        m=0
        for i in range(s1):
            if(s[i]==c):
                break
            if(s[i]==a):
                m+=1
            if(s[i]==b):
                m-=1
        k=a1-b1
        for i in range(c1-1):
            print(1)
        if(k>=c1):
            if(c1==1):
                if(k-c1+1>m):
                    print(-1)
                else:
                    print(k-c1+1)
            else:
                print(k-c1+1)





