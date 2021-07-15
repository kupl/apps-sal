x,y=map(int,input().split())
g1 = {1,3,5,7,8,10,12}
g2 = {4,6,9,11}
g3 = {2}

def group(z):
  if z in g1:return 1
  elif z in g2:return 2
  else: return 3
  
if group(x)==group(y):print('Yes')
else:print('No')
