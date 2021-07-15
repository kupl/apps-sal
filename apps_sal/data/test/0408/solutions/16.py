n,m=input().split()
n=int(n)
m=int(m)
k=0
while n+m>2 and n>0 and m>0:
    if m<2*n:
        m-=1
        n-=2
        k+=1
    else:
        n-=1
        m-=2
        k+=1
print(k)    
