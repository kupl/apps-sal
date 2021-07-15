import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  h,w,x,y = map(int,input().split())
  can = [h*y,h*(w-1-y),w*x,w*(h-1-x)]
  print(max(can))
