s,c=map(int,input().split())

if c>=s*2:
  ans=s+(c-s*2)//4
  
else:
  ans=c//2
  
print(ans)
