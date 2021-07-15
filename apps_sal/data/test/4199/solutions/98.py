N,K=map(int,input().split())
H=list(map(int,input().split()))
answer=0

for i in range(N):
  if H[i]>=K:
    answer+=1
print(answer)
