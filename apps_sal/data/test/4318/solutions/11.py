A=int(input())
l=list(map(int,input().split()))
ans=0
f=0
for i in l:
   if f<=i:
      f=i
      ans+=1
print(ans)
