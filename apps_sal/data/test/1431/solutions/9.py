N = int(input())
A = [0] + list(map(int,input().split()))
ans = [0]*(N+1)
for i in reversed(range(1,N+1)):
  tot = 0
  for j in range(i+i,N+1, i):
    tot+=ans[j]
  if tot%2 != A[i]:
    ans[i] = 1
M = sum(ans)
res = []
for i in range(1,N+1):
  if ans[i] == 1:
    res.append(str(i))
print(M)
print(' '.join(res))
