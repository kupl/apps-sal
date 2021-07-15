import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int,readline().split()))

ans = [0] * N

for i in range(len(A)):
  ans[A[i] - 1] += 1
  
for a in ans:
  print(a)
