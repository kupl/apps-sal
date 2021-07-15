N, M = map(int, input().split())
A = ["x"]*N
for i in range(M):
  s, c = map(int, input().split())
  if A[s-1] == "x":
    A[s-1] = c
  elif A[s-1] != c:
    print(-1)
    return


if A[0]==0 and N>1:
  print(-1)
  return
elif N==1 and (A[0]=="x" or A[0] == 0):
  print(0)
  return
elif A[0]=="x" or A[0] == 0:
  A[0]=1

for i in range(1,N):
  if A[i]=="x":
    A[i]=0

ans = 0
if A[0]>0:
  for i in range(N):
    ans += A[i]*10**(N-i-1)
else:
  ans = -1
  
print(ans)
