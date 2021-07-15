n=int(input())
if n==0:
  print((0))
  return
ans=[]
while n!=0:
  n-=1
  ans.append(n%-2)
  n//=(-2)
#print(ans)
tmp=[1*(i==0) for i in ans][::-1]
print(("".join(map(str,tmp))))

