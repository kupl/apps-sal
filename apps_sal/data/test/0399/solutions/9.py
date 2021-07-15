import sys

#f = open('input', 'r')
f = sys.stdin

x,y = list(map(int, f.readline().split()))

if y>0 and x>=y-1 and (x-y+1)%2==0:
  if x>0 and y==1:
    print('No')
  else:
    print('Yes')
else:
  print('No')

