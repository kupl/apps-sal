n,k=list(map(int,input().split()))

#a=b*x+kk  (k<kk<b)

if k==0:
    print((n**2))
    return

cnt=0
for b in range(k+1,n+1):
    ux=n//b
    if n%b==0:
        umod=0
    else:
        umod=max(0,n%b-k+1)
    dmod=max(0,b-k)
    #print(b,"##############")
    #print(umod,dmod)

    cnt+=umod+dmod*(ux)

print(cnt)

