a,b,x=map(int,input().split())
l,r=0,10**9+1
while r-l>1:
  t=(l+r)//2
  r,l=[[r,t],[t,l]][a*t+b*(len(str(t)))>x]
print(l)
