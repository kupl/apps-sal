N=int(input())
P=list(map(int,input().split()))
cnt=0
for n in range(N):
  if (n+1)!=P[n]:
    cnt+=1

if cnt<=2:
  print("YES")
else:
  print("NO")
