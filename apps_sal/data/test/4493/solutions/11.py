c=[]
for _ in range(3):
    c.append(list(map(int,input().split())))

s=0
for i in range (3):
    for j in range(3):
        if i==j:
            s+=c[i][j]*2
        else:s-=c[i][j]

if s==0:print("Yes")
else:print("No")

