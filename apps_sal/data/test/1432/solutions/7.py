N=int(input())
A=list(map(int,input().split()))

X0=0

for i in range(N):
  if i%2==0:
    X0+=A[i]
  else:
    X0-=A[i]

ans=[X0]

for i in A:
  ans.append((i-ans[-1]//2)*2)
print(*ans[:-1])
