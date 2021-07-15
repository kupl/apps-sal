N = int(input())
MOD = 10 ** 9 + 7

memo = [{} for i in range(N+1)]

def f(x):
  for i in range(4):
    temp = list(x)
    if i >= 1:
      temp[i-1], temp[i] = temp[i], temp[i-1]
    if ''.join(temp).count('AGC') >= 1:
      return False
  return True

def dfs(temp, x):
  if x in memo[temp]:
    return memo[temp][x]
  if temp == N:
    return 1
  ans = 0
  for c in 'ACGT':
    if f(x + c):
      ans = (ans + dfs(temp + 1, x[1:] + c)) % MOD
  memo[temp][x] = ans
  return ans

print(dfs(0, 'XXX'))
