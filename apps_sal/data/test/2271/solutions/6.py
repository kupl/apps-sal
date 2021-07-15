n=int(input())
p=[[]]
t=[0]
o=[[]]
for i in range(n):
    p.append([])
    t.append(0)
    o.append([])
for i in range(n-1):
    a=input().split()
    b=int (a[0])
    c=int(a[1])
    p[b].append(c)
    p[c].append(b)
    t[b]+=1
    t[c]+=1
y=0
for i in range(1,n+1):
    j=p[i]
    for k in range(t[i]):
        jj=j[k]
        y=y+t[jj]-1
print(int(y/2))


