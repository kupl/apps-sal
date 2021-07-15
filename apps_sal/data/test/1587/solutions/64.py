n=int(input())
s=input()
w=s.count('W')
r=s.count('R')

ans=10**9
if w==0 or r==0:
  print(0)
  return

left_white, right_red=0,r
for i in range(n):
  if s[i]=='W':
    left_white+=1
  else:
    right_red-=1
  ans=min(ans,max(left_white,right_red))
  
print(ans)
