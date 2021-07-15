N = int(input())
A = [int(x) for x in input().split()]
 
s_sum = sum(A)
 
ans = [None] * N
 
ans[0] = s_sum
for i in range(1, N, 2):
  ans[0] -= 2 * A[i]
 
for i in range(N-1):
  ans[i + 1] = 2 * A[i] - ans[i]
 
print(*ans)
