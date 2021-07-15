a,b,x,y=map(int,input().split())
if a==b:print(x)
if a>b:print(min(x+(a-b-1)*y,x+(a-b-1)*2*x))
if a<b:print(min(x+(b-a)*y,(2*(b-a)+1)*x))
