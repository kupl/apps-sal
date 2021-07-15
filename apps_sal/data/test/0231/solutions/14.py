x,y=[int(i) for i in input().split()]
r=1
if y % 2==0:
    for i in range(x,1,-2):
        if i==y:
            break
        else:
            r+=1
else:
    for i in range(1,x,+2):
        if i==y:
            break
        else:
            r+=1
print(r)

