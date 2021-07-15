N = int(input())
P = list(map(int,input().split()))
c = 0

for n in range(N-1):
  if P[n]==n+1:
    P[n],P[n+1] = P[n+1],P[n]
    c+=1

if P[-1]==N:
  print(c+1)
else:
  print(c)
