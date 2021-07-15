from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
L = defaultdict(int)
ans = 0
for i in range(N):
  L[i+1 - A[i]]+=1
for i in range(N):
  ans+=L[i+1+A[i]]
print(ans)


