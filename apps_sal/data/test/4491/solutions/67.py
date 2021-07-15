N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
  ans = max(ans, sum(A[:i+1])+sum(B[i:]))
print(ans)
