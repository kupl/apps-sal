a,b=list(map(int,input().split()))
res=0
while a!=0 and b!=0:
    if a>=b:
        res+=a//b
        a=a%b
    elif b>a:
        res+=b//a
        b=b%a
print(res)

