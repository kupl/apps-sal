

def f(a):
  n = len(a)
  dp = [0] * n
  
  s = [0] * (n+1)
  
  for i in range(0, n):
    s[i+1] = s[i] + a[i]

  #print(s)

  maxdiffyet = s[n]

  #print(f"maxdiffyet = {maxdiffyet}")

  for i in range(n-2, -1, -1):
    dp[i] = maxdiffyet
    #print(f"dp[{i}] = {dp[i]}, s[{i}] = {s[i]}, maxdiffyet({i}) = {maxdiffyet} -> {max(maxdiffyet, s[i+1] - dp[i])}")
    maxdiffyet = max(maxdiffyet, s[i+1] - dp[i])

  #print(dp)

  return dp[0]


n = int(input())
a = [int(x) for x in input().split(' ')]

print(f(a))

