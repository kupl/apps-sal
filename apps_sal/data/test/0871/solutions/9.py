n,s=map(int,input().split())
time=[0]*n
for i in range(n):
  h,m=map(int,input().split())
  time[i]=h*60+m

gogo=0
if time[0]-1-gogo>=s:
  print(0,0)
  return

fail=True
for i in range(n-1):
  gogo=time[i]+1+s
  if time[i+1]-gogo-1>=s:
    ans=gogo
    fail=False
    break

if fail: gogo=time[-1]+s+1 
hour=gogo//60
min=gogo%60
print(hour,min)
