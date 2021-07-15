import sys,os,io
input = sys.stdin.readline
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
T = int(input())
ans = [0]*T
for t in range(T):
  N = int(input())
  A = list(map(int, input().split()))
  L = list(map(int, input().split()))
  B = [A[i] for i in range(N) if L[i]==0]
  B.sort()
  ans[t] = []
  for i in range(N):
    if L[i]==0:
      ans[t].append(B.pop())
    else:
      ans[t].append(A[i])
for a in ans:
  print(*a)
