def gcd(n,m):
    if m==0:
        return n
    else:
        return gcd(m,n%m)

N=int(input())
count=0
m=2
while m*m<=N:
    for n in range(1,m):
        a=m*m-n*n
        b=2*m*n
        c=m*m+n*n
        if c>N:
            break
        if gcd(m,n)==1 and (m+n)%2==1:
            count+=(N//c)
        #print(a,b,c)
    m+=1
print(count)
