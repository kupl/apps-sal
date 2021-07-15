import heapq

n = int(input())
A = list(map(int, input().split()))
Left_top = A[:n]
Right_bottom = [-i for i in A[-n:]]
L = [0]*(n+1)
R = [0]*(n+1)
L[0] = sum(Left_top)
R[-1] = sum(Right_bottom)
heapq.heapify(Left_top)
heapq.heapify(Right_bottom)
for i in range(n, 2*n):
  L[i-n+1] = L[i-n] - heapq.heappushpop(Left_top, A[i]) + A[i]
  R[2*n-i-1] = R[2*n-i] - heapq.heappushpop(Right_bottom, -A[-(i+1)]) - A[-(i+1)]
ans = -float("inf")
for i in range(n+1):
  ans = max(ans, L[i] + R[i])
print(ans)
