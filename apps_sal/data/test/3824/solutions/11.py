x1,y1=[int(i) for i in input().split()]
x2,y2=[int(i) for i in input().split()]
if (x1==x2):
    print (4+2*(abs(y1-y2)+1))
elif (y1==y2):
    print (4+2*(abs(x1-x2)+1))
else:
    print (2*(abs(x1-x2)+1) + 2*(abs(y1-y2)+1))
