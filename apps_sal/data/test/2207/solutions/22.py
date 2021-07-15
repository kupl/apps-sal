r,c=list(map(int,input().split()))
a=[]
for i in range(r):
    a.append(input())
b=[]
for i in range(c):
    e=0
    for j in range(r):
        if a[j][i]=="B":
            e=1
    b.append(e)
d=0
e=0
for i in range(c):
    if b[i]==1:
        d+=1
    if b[i]==0 and d!=0:
        d=0
        e+=1
if d!=0:
    print(e+1)
else:
    print(e)
