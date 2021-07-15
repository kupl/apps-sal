def gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else :
            b=b-a
    print(m//a,'/',n//a,sep='')
a,b,c,d=map(int,input().split())
m=1
n=1

if a==b:
    if c==d :
        print(0,'/',1,sep='')
    else :
        if c>d:
            m=b*c-a*d
            n=c*b
            gcd(m,n)
        else :
            m=a*d-c*b
            n=a*d           
            gcd(m,n)
else:
    if c/d ==a/b:
        print(0,'/',1)
    else :
        if c/d>a/b:
            m=b*c-a*d
            n=c*b
            gcd(m,n)
        else :
            m=a*d-c*b
            n=a*d           
            gcd(m,n)        
            
        
                 

