N=int(input())
P=list(map(int,input().split()))
count=0
for i in range(0,N-2):
  max_P=max(P[i],P[i+1],P[i+2])
  min_P=min(P[i],P[i+1],P[i+2])
  if P[i+1] != max_P and P[i+1] != min_P:
    count+=1
print(count)
