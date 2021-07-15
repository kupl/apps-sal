N = int(input())
P = list(map(int,input().split()))
ans = 0

for n in range(N-1):
  if P[n]==n+1 and P[n+1]==n+2:
    ans+=1
    P[n+1] = n+1
  elif P[n]==n+1 and P[n+1]!=n+2:
    ans+=1

if P[-1]==N:
  print(ans+1)
else:
  print(ans)
