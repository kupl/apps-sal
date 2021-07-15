info=list(map(int,input().split()))
t=info[0]
s=info[1]
q=info[2]
q=(q-1)/q
p=s
ans=0
while p<t:

    p=p/(1-q)
    if ((int(p)+1)-p)<.005:
        p=int(p)+1
    ans+=1
    
print(ans)    

