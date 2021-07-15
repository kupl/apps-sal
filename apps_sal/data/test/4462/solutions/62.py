n=int(input())
l=list(map(int,input().split()))
x,y,z=0,0,0
for a in l:
    if a%4==0:
        z+=1
    elif a%2==0:
        y+=1
    else:
        x+=1
if y>0:
    x+=1
print(('Yes'if x<=z+1 else'No'))

