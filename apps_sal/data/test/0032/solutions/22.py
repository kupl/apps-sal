from sys import stdin

n=int(stdin.readline())
flag=False
LIMITE=20*1000
x,y=0,LIMITE
for i in range(n):
    d,direc=stdin.readline().split()
    d=int(d)
    if (y==LIMITE and direc!="South") or (y==0  and direc!="North") or y<0 or y>LIMITE :
        flag=True
        
    if direc=="South":
        y-=d
    elif direc=="North":
        y+=d
    elif direc=="East":
        x+=d
    else:
        x-=d

    
if y!=LIMITE:
    flag=True
if flag:
    print("NO")
else:
    print("YES")
    

