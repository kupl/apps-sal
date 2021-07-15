x=int(input())
ans=0
ans+=2*(x//11)
if x%11<=6 and x%11!=0:
  ans+=1
elif x%11!=0 and 7<=x%11:
  ans+=2
print(ans)
