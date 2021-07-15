n=int(input())
ans=1
for i in range(5):
  ans=ans*(n-i)*(n-i)
ans=ans//(2*3*4*5)
print(ans)
