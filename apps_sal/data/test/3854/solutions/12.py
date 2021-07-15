import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

DP = [[False]*(k+2) for _ in range(k+2)]

DP[0][0] = True

for a in sorted(A):
  for i in range(k, a-1, -1):
    for j in range(0, k+1):
      DP[i][j] |= DP[i-a][j]
      if j >= a:
        DP[i][j] |= DP[i-a][j-a]

print(sum(DP[k]))
for i in range(k+1):
  if DP[k][i]:
    print(i)

