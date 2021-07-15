k=int(input())
i=0
r=1
while(k>=r):
    r+=9*(i+1)*10**i
    i+=1
r=r-(9*i*10**(i-1))
ans=str(((k-r)//i)+10**(i-1))[(k-r)%i]
print(ans)

