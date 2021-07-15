n,m=map(int,input().split())
i,d=0,[1]*(n+1)
while i<n:d[i+1]=((m-i)*((m-n+i)*d[i]+i*d[i-1]*(m-i+1)))%(10**9+7);i+=1
print(d[-1])
