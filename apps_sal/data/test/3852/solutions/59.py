ans = 0
N = int(input())
A = list(map(int, input().split()))
ans = []
M = -float('inf')
m = float('inf')
for i in range(N):
  if A[i]>M:
    M_ind = i+1
    M = A[i]
  if A[i]<m:
    m_ind = i+1
    m = A[i]
if M*m<0:
  for i in range(N):
    if M>=abs(m):
      if i+1!= M_ind:
        ans.append([M_ind,i+1])
        A[i] += M
    else:
      if i+1!= m_ind:
        ans.append([m_ind,i+1])
        A[i] += m
if max(A)>0:
  for i in range(1,N):
    ans.append([i,i+1])
else:
  for i in range(N,1,-1):
    ans.append([i,i-1])
print(len(ans))
for a in ans:
  print(*a)
