n,x=map(int,input().split())

def func(m,y):
  if y==0:return 0
  ret=0
  t=4*pow(2,m)-3
  if y>=t-1:
    ret=pow(2,m+1)-1
  elif y==(t-1)//2:
    ret=pow(2,m)-1
  elif y==(t-1)//2+1:
    ret=pow(2,m)
  elif y>(t-1)//2+1:
    ret=pow(2,m)
    ret+=func(m-1,y-(t-1)//2-1)
  else:
    ret=func(m-1,y-1)
  return ret

print(func(n,x))
