N=int(input())
cnt=0
for i in range(N+1):
  S=str(i)
  if len(S)%2==1:
    cnt+=1
print(cnt-1)
