n=int(input())
a=-2*10**9
b=2*10**9
for i in range(n):
    s=input().split()
    x=int(s[1])
    ans=str(s[2])
    s=s[0]
    if(s==">="):
        if(ans=="Y"):
            a=max(a,x)
        else:
            b=min(b,x-1)
    elif(s=="<="):
        if(ans=="Y"):
            b=min(b,x)
        else:
            a=max(a,x+1)
    elif(s=="<"):
        if(ans=="Y"):
            b=min(b,x-1)
        else:
            a=max(x,a)
    elif(s==">"):
        if(ans=="Y"):
            a=max(a,x+1)
        else:
            b=min(x,b)
if(b<a):
    print("Impossible")
else:
        
    print(b)

