def main():
  n, m = map(int, input().split())
  
  dp = [0]*(2**n)
  len_dp = len(dp)

  key_list = dict()
  sub = 1
  for i in range(n):
    key_list[i+1] = sub
    sub *= 2

  for _ in range(m):
    a, b = map(int, input().split())
    c = [int(x) for x in input().split()]
    key = 0
    for value in c:
      key += key_list[value]
    for i in range(len_dp-1, -1, -1):
      if i == 0 or dp[i]:
        if dp[i|key]:
          dp[i|key] = min([dp[i]+a, dp[i|key]])
        else:
          dp[i|key] = dp[i]+a

  print(dp[len_dp-1] if dp[len_dp-1] else -1)

def __starting_point():
  main()
__starting_point()
