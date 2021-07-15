a=[i for i,j in enumerate(input(),1) if j=='1']
m=int(input())
q=[(-1,0,0,[])]
p='NO'
while q:
    x,y,z,t=q.pop()
    if z==m:
        p='YES\n'+' '.join(map(str,t))
        break
    for i in a:
        if i!=x and i>y:
            q.append((i,i-y,z+1,t+[i]))
print(p)
