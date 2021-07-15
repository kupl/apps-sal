n=int(input())
w=list(map(int,input().split()))
sum=int(0)
for i in range(n):
  sum+=w[i]
dif=sum
for i in range(n):
  psum=int(0)
  for j in range(i):
    psum+=w[j]
  dif=min(dif,abs(psum-(sum-psum)))
print(dif)

