def main():
  N = int(input())
  INF = float('inf')
  A = [(i+1, a) for i, a in enumerate(map(int, input().split()))]
  A = sorted(A, key=lambda x: x[1], reverse = True)
 
  dp = [[-INF] * (N+1) for _ in range(N+1)]
  dp[0][0] = 0
 
  for s in range(1, N+1):
    for l in range(s+1):
      r = s - l
      dp[l][r] = max(dp[l-1][r] + A[s-1][1] * abs(A[s-1][0]-l), dp[l][r-1] + A[s-1][1] * abs(N-r+1-A[s-1][0]))
    
  ans = 0
  for m in range(N):
    if(dp[m][N-m] > ans):
      ans = dp[m][N-m]
    
  print(ans)
 
main()
