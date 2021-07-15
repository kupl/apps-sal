_=int(input())
a=list(map(int,input().split()))

x,y,z=0,0,0
for i in a:
    if i%4 == 0:
        z+=1
    elif i%2 == 0:
        y+=1
    else:
        x+=1
if y:
    if x <= z:
        print('Yes')
    else:
        print('No')
else:
    if x <= z+1:
        print('Yes')
    else:
        print('No')
