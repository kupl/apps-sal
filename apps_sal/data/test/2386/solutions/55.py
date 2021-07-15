n = int(input())
A = list(map(int, input().split()))
for i in range(n):
  A[i] = A[i] - (i+1)

A.sort()
b = A[n//2]

ans = 0
for i in range(n):
  ans += abs(A[i] -b)
print(ans)
