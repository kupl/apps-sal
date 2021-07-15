N,X=map(int,input().split())

def n_pati(l):
  val = 1
  for i in range(l):
    val = val*2+1
  return val

def n_layer(l):
  val = 1
  for i in range(l):
    val = val*2+3
  return val

SUM=0
while 1:
  if N==1:
    if X in [0,1]:break
    elif X>=2:
      SUM += min(3,X-1)
      break
  
  L = n_layer(N)
  if X >= L//2:
    SUM += n_pati(N-1)
    X -= n_layer(N-1)+1
    if X==0:
      break
    SUM += 1
    X -= 1
    if X==0:
      break
    N -= 1
  else:
    X -= 1
    N -= 1
    
  if X in [0,1]:break
  
print(SUM)
