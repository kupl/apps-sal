n=int(input())
s=int(input())
def fun(b,n):
    if n<b:
        return n
    else:
        return fun(b,n//b)+n%b
if n<s:
    print(-1)
elif n==s:
    print(n+1)
else:
    for b in range(2,int(n**0.5)+1):
        if fun(b,n)==s:
            print(b)
            return
    yaku=set()
    for x in range(1,int((n-s)**0.5)+1):
        if (n-s)%x==0:
            yaku|={x,(n-s)//x}
    ans=n+2
    for k in yaku:
        b=(n-s)//k+1
        l=s-k
        if 0<=l<b and n<b**2 and k+l==s:
            ans=min(ans,b)
    if ans>n:
        print(-1)
    else:
        print(ans)
