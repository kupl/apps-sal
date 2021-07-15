N = int(input())
Ps = list(map(int,input().split()))
cnt = 0
for i in range(1,N-1):
  if Ps[i-1] < Ps[i]<Ps[i+1] or Ps[i+1] < Ps[i]<Ps[i-1]:
    cnt+=1
print(cnt)
