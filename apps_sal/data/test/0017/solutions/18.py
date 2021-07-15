n,k,t=map(int, input().split())
if(t<k):
  print(t)
elif(t<=n and t>=k):
  print(k)
else:
  print(k-(t-n))
