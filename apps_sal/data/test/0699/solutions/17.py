y,k,n=[int(i) for i in input().split()]

a=y%k
m=[]
for i in range(n):
    h=i*k-a
    num=h+y
    if num<=n:
        if h>0:
            m.append(h)
    else:break
if len(m)>0:
    print(*m)
else:print(-1)



