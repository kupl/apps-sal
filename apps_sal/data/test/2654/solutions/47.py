N = int(input())

A = []
B = []
for i in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)
A.sort()
B.sort()

if N%2:
  ma = A[N//2]
  mb = B[N//2]
  print(max(0, mb-ma+1))
else:
  ma = A[N//2] + A[N//2-1]
  mb = B[N//2] + B[N//2-1]
  print(max(0, mb-ma+1))
