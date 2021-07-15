def solve(A):
  d = {}
  for a in A:
    if a in d:
      d[a] += 1
    else:
      d[a] = 1
  
  for a in d:
    if d[a] % 2:
      return 'First'
  return 'Second'


T = int(input())
ans = []
for i in range(T):
  N = int(input())
  A = list(map(int, input().split()))
  if N % 2:
    ans.append('Second')
  else:
    ans.append(solve(A))

print(*ans, sep='\n')
