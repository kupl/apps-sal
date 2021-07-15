t = int(input())
for i in range(t):
  #a-x-2y=0
  #b-2x-y=0
  #x=a-2y
  #b-2(a-2y)-y=0
  #b-2a+3y=0
  #y=(2a-b)/3
  a,b=map(int,input().split())
  if (2*a-b)%3==0 and (2*a-b>=0) and (2*b-a>=0):
    print("YES")
  else:
    print("NO")
