N = int(input())
A = []; B = []
for i in range(N):
  a,b = map(int,input().split())
  A.append(a);B.append(b)

A.sort();B.sort()
if N%2 == 0:
  MIN = A[N//2-1]+A[N//2] #Medianの二倍
  MAX = B[N//2-1]+B[N//2]
  ans = MAX-MIN+1
else:
  MIN = A[N//2] #Medianの二倍
  MAX = B[N//2]
  ans = MAX-MIN+1
print(ans)
