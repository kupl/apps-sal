N = int(input())
A = [int(a) for a in input().split()]
ans = [0] * N
for i in range(N):
  ans[A[i] - 1] = i + 1
print(*ans)
