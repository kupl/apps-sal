import math
N=int(input())

def get_circle_2p(p1,p2):
  x1,y1=p1
  x2,y2=p2
  
  x=(x1+x2)/2
  y=(y1+y2)/2  
  rad=math.sqrt((x1-x2)**2+(y1-y2)**2)/2
  return x,y,rad

def get_circle_3p(p1,p2,p3):
  x1,y1=p1
  x2,y2=p2
  x3,y3=p3
  d=2*((y1-y3)*(x1-x2)-(y1-y2)*(x1-x3))  
  
  if d==0:
    rad1=math.sqrt((x1-x2)**2+(y1-y2)**2)/2
    rad2=math.sqrt((x1-x3)**2+(y1-y3)**2)/2
    rad3=math.sqrt((x2-x3)**2+(y2-y3)**2)/2
    
    if rad1>=rad2 and rad1>=rad3:
      x=(x1+x2)/2
      y=(y1+y2)/2
      return x,y,rad1
    elif rad2>=rad1 and rad2>=rad3:
      x=(x1+x3)/2
      y=(y1+y3)/2
      return x,y,rad2
    elif rad3>=rad1 and rad3>=rad2:
      x=(x2+x3)/2
      y=(y2+y3)/2
      return x,y,rad3      
  else:
    x=((y1-y3)*(y1**2-y2**2+x1**2-x2**2)-(y1-y2)*(y1**2-y3**2+x1**2-x3**2))/d
    y=((x1-x3)*(x1**2-x2**2+y1**2-y2**2)-(x1-x2)*(x1**2-x3**2+y1**2-y3**2))/-d
    r=math.sqrt((x-x1)**2+(y-y1)**2)
    return (x,y,r)
  
xylist=[]
for i in range(N):
  xi,yi=map(int,input().split())
  xylist.append((xi,yi))
  
#print(xylist)

if N==2:
  x,y,r=get_circle_2p(xylist[0],xylist[1])
  print(r)
else:
  min_radius=float("inf")
  for i in range(N):
    for j in range(i+1,N):
      #print(xylist[i],xylist[j])
      x,y,r=get_circle_2p(xylist[i],xylist[j])
      #print(x,y,r)
      if r>min_radius:
        continue
      
      for l in range(N):
        if l==i or l==j:
          continue
          
        xl,yl=xylist[l]
        diff_xl=xl-x
        diff_yl=yl-y
        if math.sqrt(diff_xl**2+diff_yl**2)>r:
          break
      else:
        if r<min_radius:
          min_radius=r
  
  for i in range(N):
    for j in range(i+1,N):
      for k in range(j+1,N):
        #print(xylist[i],xylist[j],xylist[k])
        x,y,r=get_circle_3p(xylist[i],xylist[j],xylist[k])
        #print(x,y,r)
        if r>min_radius:
          continue
        
        for l in range(N):
          if l==i or l==j or l==k:
            continue
            
          xl,yl=xylist[l]
          diff_xl=xl-x
          diff_yl=yl-y
          if math.sqrt(diff_xl**2+diff_yl**2)>r:
            break
        else:
          if r<min_radius:
            min_radius=r
  
  print(min_radius)
