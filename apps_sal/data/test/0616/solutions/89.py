def main():
  N, M = map(int, input().split())
  inf =  10**9
  p = 1<<N
  dp = [inf]*p 
  dp[0] = 0
  for i in range(M):
    a, b = map(int, input().split())
    C = list(map(int, input().split()))
    c_bit = sum([1<<(c-1) for c in C])
    for j in range(p):
      #print(min(dp[i][j|c_bit], dp[i][j] + a))
      dp[j|c_bit] = min(dp[j|c_bit], dp[j] + a)
  if dp[p-1] == inf:
    print(-1)
  else: 
    print(int(dp[p-1]))
  
def __starting_point():
  main() 
__starting_point()
