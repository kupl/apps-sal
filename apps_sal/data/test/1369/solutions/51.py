import numpy as np

N = int(input())
x_lis = []
y_lis = []

for i in range(N):
  num_x, num_y = map(int, input().split())
  x_lis.append(num_x)
  y_lis.append(num_y)

def a(X,Y,Z):
  A = np.dot(Y-Z,Y-Z)
  B = np.dot(Z-X,Z-X)
  C = np.dot(X-Y,X-Y)

  T = A*(B+C-A)
  U = B*(C+A-B)
  W = C*(A+B-C)

  if not T+U+W:
    return [10**9,10**9]
  else:
    return (T*X+U*Y+W*Z)/(T+U+W)

r = 10**9
for i in range(len(x_lis)-1):
  for j in range(i+1,len(x_lis)):
    x1 = x_lis[i]
    y1 = y_lis[i]
    x2 = x_lis[j]
    y2 = y_lis[j]
    center_x = (x1+x2)/2
    center_y = (y1+y2)/2
    dist = ((x1-x2)**2+(y1-y2)**2)**0.5/2
    if max([((center_x-i)**2+(center_y-j)**2)**0.5 for i,j in zip(x_lis, y_lis)]) == dist:
      r = min(dist, r)
    
for i in range(len(x_lis)-2):
  for j in range(i+1,len(x_lis)-1):
    for k in range(j+1,len(x_lis)):
      x1 = x_lis[i]
      y1 = y_lis[i]
      x2 = x_lis[j]
      y2 = y_lis[j]
      x3 = x_lis[k]
      y3 = y_lis[k]
      center = a(np.array([x1,y1]), np.array([x2,y2]), np.array([x3,y3]))
      dist = ((center[0]-x1)**2+(center[1]-y1)**2)**0.5
      if max([((center[0]-i)**2+(center[1]-j)**2)**0.5 for i,j in zip(x_lis,y_lis)]) == dist:
        r = min(dist, r)
      
print(r)
