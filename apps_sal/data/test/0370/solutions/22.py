k = int(input())
X,Y = map(int,input().split())
x = max(abs(X),abs(Y))
y = min(abs(X),abs(Y))
c = (k-(x+y)%k)%k
if k%2 == 0 and (x+y)%2 == 1:
  print(-1)
  return
  
import math
ans = []
m = math.ceil((x+y)/k)
if (x+y)/k == int((x+y)/k):
  for i in range(m):
    ans.append((min(x,k*i+k),max(0,k*i+k-x)))
    
elif m == 1:
  if (x+y)%2 == 1:
    ans.append((x,x-k))
    ans.append((x+(k+x-y)//2,(-k+x+y)//2))
    ans.append((x,y))
  else:
    ans.append(((x+y)//2,-k+(x+y)//2))
    ans.append((x,y))
               
elif c%2 == 0 and x+y >= k:
  a = abs((k*m-x-y)//2)
  for i in range(m-1):
    l = k*i+k
    if a >= l:
      ans.append((0,-l))
    elif a < l <= x+a:
      ans.append((l-a,-a))
    elif x+a < l:
      ans.append((x,l-x-2*a))
  ans.append((x,y))
  
else:
  m += 1
  a = abs((k*m-x-y)//2)
  for i in range(m-1):
    l = k*i+k
    if a >= l:
      ans.append((0,-1))
    elif a < l <= x+a:
      ans.append((l-a,-a))
    elif x+a < l:
      ans.append((x,l-x-2*a))
  ans.append((x,y))
  
print(len(ans))
for i,j in ans:
  if abs(X) < abs(Y):
    i,j = j,i
  if X < 0:
    i *= -1
  if Y < 0:
    j *= -1
  print(i,j)
