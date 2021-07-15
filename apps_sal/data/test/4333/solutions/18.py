x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=100,100,100,100
if y2-y1==0 or x2-x1==0:
  if x2>x1:
    x3=x2
    y3=y2+(x2-x1)
    x4=x1
    y4=y3
  elif y2>y1:
    x3=x1-(y2-y1)
    y3=y2
    x4=x3
    y4=y1
  elif x1>x2:
    x3=x2
    y3=y2+(x2-x1)
    x4=x1
    y4=y3
  elif y1>y2:
    x3=x1-(y2-y1)
    y3=y2
    x4=x3
    y4=y1

else:
  if x2>x1 and y2>y1:
    x3=x2-(y2-y1)
    y3=y2+(x2-x1)
    x4=x3-(x2-x1)
    y4=y3-(y2-y1)
  elif x2<x1 and y2>y1:
    x3=x2-(y2-y1)
    y3=y2-(x1-x2)
    x4=x3+(x1-x2)
    y4=y3-(y2-y1)
  elif x2<x1 and y2<y1:
    x3=x2+(y1-y2)
    y3=y2-(x1-x2)
    x4=x3+(x1-x2)
    y4=y3+(y1-y2)
  elif x2>x1 and y1>y2:
    x3=x2+(y1-y2)
    y3=y2+(x2-x1)
    x4=x3-(x2-x1)
    y4=y3+(y1-y2)

print(x3,y3,x4,y4)
