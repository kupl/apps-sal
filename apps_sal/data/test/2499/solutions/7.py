import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
x = 0
for a in A:
  x ^= a
now = 0
for i in range(59, -1, -1):
  if x>>i & 1:
    continue
  for j in range(now, n):
    if A[j]>>i & 1:
      A[now], A[j] = A[j], A[now]
      for k in range(n):
        if k != now and A[k]>>i & 1:
          A[k] ^= A[now]
      now += 1
      break
b = 0
for a in A:
  b ^= a
ans = b + (x^b)
print(ans)
