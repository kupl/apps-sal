import statistics
N = int(input())
A = list(map(int,input().split()))
for i in range(N):
  A[i] -= i+1
A.sort()
b = statistics.median(A)
s = 0
for i in range(N):
  s += abs(A[i] - b)
print(int(s))  
