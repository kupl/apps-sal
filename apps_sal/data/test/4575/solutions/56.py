N = int(input())
D, X = [int(x) for x in input().split()]
A = [int(input()) for _ in range(N)]
ans = X
for i in range(N):
  a = 1
  l = 1
  while a <= D:
    ans += 1
    a = l*A[i] + 1
    l += 1
print(ans)
