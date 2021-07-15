N = int(input())
A = list(map(int,input().split()))
ans = []
flg = 0

A.sort(reverse=True)

for i in range(N-1):
  if A[i] == A[i+1] and flg == 0:
    ans.append(A[i])
    flg = 1
  else:
    flg = 0

if len(ans) > 1:
  print(ans[0]*ans[1])
else:
  print(0)
