N = int(input())
P = list(map(int, input().split()))
ans = []
left = 0
while left<N-1:
  if P[left]==left+1:
    print(-1)
    return
  for i in range(left+1,N):
    if P[i]==left+1:
      for j in range(i,left,-1):
        ans.append(j)
        P[j-1], P[j] = P[j], P[j-1]
      new_left = i
      break
  for i in range(left, new_left):
    if P[i]!=i+1:
      print(-1)
      return
  left = new_left
print(*ans, sep='\n')

