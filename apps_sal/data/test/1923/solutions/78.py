N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(0, 2 * N, 2):
  ans += A[i]
print(ans)
