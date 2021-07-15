N = int(input())
A = list(map(int, input().split()))
 
ans = [0]*N
for i in range(N):
  ans[A[i]-1] = str(i+1)

for i in range(N):
  print(ans[i], end=' ')
