import numpy as np

def RPS(s1, s2):
  if s1 == s2:
    return s1
  elif set([s1, s2]) == set(["R", "P"]):
    return "P"
  elif set([s1, s2]) == set(["P", "S"]):
    return "S"
  elif set([s1, s2]) == set(["S", "R"]):
    return "R"

def main():
  N, K = map(int, input().split())
  s = str(input())
  dp = [[0]*N for _ in range(K+1)]
  for i in range(N):
    dp[0][i] = s[i]
  for k in range(1, K+1):
    for i in range(N):
      dp[k][i] = RPS(dp[k-1][2*i%N], dp[k-1][(2*i+1)%N])
  print(dp[K][0])
      
def __starting_point():
  main()
__starting_point()
