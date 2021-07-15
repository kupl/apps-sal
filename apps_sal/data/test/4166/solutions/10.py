N,M=map(int,input().split())

arr = [-1] * N
S = []
C = []
for _ in range(M):
  s,c = map(int,input().split())
  S.append(s-1)
  C.append(c)

def replace(arr, f, t):
  for i in range(len(arr)):
    if arr[i] == f:
      arr[i] = t
  return arr
    
ok = True
for s, c in zip(S,C):
  if not (arr[s] == -1 or arr[s] == c):
    ok = False
    break
  arr[s] = c
if 1 < N and arr[0] == 0:
  ok = False
if ok:
  if 1 < N and arr[0] == -1:
    arr[0] = 1
  arr = replace(arr, -1, 0) 
  print(*arr, sep="")
else:
  print(-1)
