N, M = map(int, input().split())
if N < M:
  print('No')
else:
  A = [input() for _ in range(N)]
  B = ''
  cnt = 0
  for _ in range(M):
    B += input().rstrip()
  for i in range(N-M+1):
    if cnt==1:
      break
    for j in range(N-M+1):
      judge = ''
      for k in range(M):
        judge += A[i+k][j:j+M]
      if judge == B:
        cnt += 1
        break
  if cnt == 1:
    print('Yes')
  else:
    print('No')
