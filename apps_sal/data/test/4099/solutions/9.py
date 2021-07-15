N,K,M=map(int,input().split())
A=list(map(int,input().split()))
answer=0
Sum=0
for i in range(N-1):
  Sum+=A[i]

a=M*N-Sum
if a<=0:
  print(0)
elif a<=K:
  answer=a
  print(answer)
else:
  print(-1)
