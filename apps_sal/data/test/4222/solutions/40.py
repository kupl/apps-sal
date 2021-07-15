n,k = map(int,input().split())
a = [0]*(n+1)
answer = 0
for i in range(k):
  d = int(input())
  b = list(map(int,input().split()))
  for j in range(d):
    a[b[j]] +=1
for q in range(1,n+1):
  if(a[q]==0):
    answer +=1
print(answer)
