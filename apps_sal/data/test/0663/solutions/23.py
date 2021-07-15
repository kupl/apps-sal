from math import ceil, hypot

r,x,y,xx,yy = list(map(float, input().split()))
print(ceil(hypot(xx-x, yy-y)/2/r))

