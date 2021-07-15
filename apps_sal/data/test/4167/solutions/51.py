n,k=map(int,input().split())

am = [0]*k
for i in range(1, n+1):
  res = i%k
  if (res+res)%k==0:
    am[res]+=1

#print(am)

ans = 0
for i in am:
  ans += i**3 
  
print(ans)
