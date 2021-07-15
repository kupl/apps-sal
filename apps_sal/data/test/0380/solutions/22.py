x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
if x1==x2==x3 or y1==y2==y3:
    print(1)
    quit()
elif  (y1==y2 and ((x3<=x1 and x3<=x2) or (x3>=x1 and x3>=x2)))\
        or (y1==y3 and ((x2<=x1 and x2<=x3) or (x2>=x1 and x2>=x3)))\
        or (y2==y3 and ((x1<=x2 and x1<=x3) or (x1>=x2 and x1>=x3)))\
        or (x1==x2 and ((y3<=y1 and y3<=y2) or (y3>=y1 and y3>=y2)))\
        or (x1==x3 and ((y2<=y1 and y2<=y3) or (y2>=y1 and y2>=y3)))\
        or (x2==x3 and ((y1<=x2 and y1<=y3) or (y1>=y2 and y1>=y3))):
    print(2)
    quit()
else:print(3)
