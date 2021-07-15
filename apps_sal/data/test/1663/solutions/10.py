def inv(x):
    return pow(x,1000000005,1000000007)
s=input()
ans=0
n=len(s)
for i in range(n-1,-1,-1):
    z=pow(10,n-1-i,1000000007)*int(s[i])
    z=z*((i)*(i+1))//2
    ans+=z
    ans%=1000000007
    k=n-1-i
    op=0
    op+=(pow(10,k,1000000007)*(9*k-1))
    op%=1000000007
    op+=1
    op=op*inv(81)
    op%=1000000007
    op=op*int(s[i])
    ans+=op
    ans%=1000000007
print(ans)

