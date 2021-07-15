N = int(input())
*A,=map(int,input().split())
A = sorted(A)

if N == 1:
  print(1)
  return

flag = [0]*(10**6+5)
for i in range(N):
  flag[A[i]] = 1

for i in range(N):
  if flag[A[i]] == 0:
    continue
  if i>0 and A[i]==A[i-1]:
    flag[A[i]] = 0
    continue
  for num in range(A[i]*2,A[-1]+1,A[i]):
    flag[num] = 0
  
print(sum(flag))
