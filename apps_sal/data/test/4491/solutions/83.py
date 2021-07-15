N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]

# 高々N通り
# A[0][0] + (A[1][0] + ... + A[1][N-1])
# (A[0][0] + A[0][1]) + (A[1][1] + ... + A[1][N-1])
# (A[0][0] + A[0][1] + A[0][2]) + (A[1][2] + ... + A[1][N-1])
# (A[0][0] + ...+ A[0][N-1]) + A[1][N-1]

# N=100 => O(N^2)で間に合う
ans = 0
for i in range(N):
  ans = max(ans, sum(A[0][:i+1]) + sum(A[1][i:]))
  
print(ans)
