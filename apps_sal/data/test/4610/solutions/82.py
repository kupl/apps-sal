N, K = map(int, input().split())
A = list(map(int, input().split()))

A_dic = {}
A_count = []

for i in range(N):
  if A[i] not in A_dic.keys():
    A_dic[A[i]] = 1
  else:
    A_dic[A[i]] += 1
    
for i in A_dic.keys():
  A_count.append(A_dic[i])
  
if len(A_count) <= K:
  print(0)
else:
  ans = 0
  A_count.sort()
  for i in range(len(A_count) - K):
    ans += A_count[i]
  else:
    print(ans)
