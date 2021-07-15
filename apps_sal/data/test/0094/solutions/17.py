3

# BEGIN template
import sys
import re
import pprint

def dbg(x,y=''):
  if len(y) > 0: y += ' = '
  sys.stderr.write('\n>>> '+y+pprint.pformat(x)+'\n')
  sys.stderr.flush()

oo = 0x3f3f3f3f3f3f3f3f
# END template

def minn(x,y):
  if x[0] < y[0]: return x
  if x[0] > y[0]: return y
  if x[1] < y[1]: return x
  if x[1] > y[1]: return y
  return x

def main():
  n = int(input())
  s = input()
  m = len(s)
  s = '0'+s
  power = [1]
  for i in range(1,61):
    power.append(power[i-1]*n)
  dp = [(int(1e70),int(1e70))]*65
  dp[m+1] = (0,0)
  for i in range(m,0,-1):
    if s[i] == '0':
      tmp = dp[i+1]
      dp[i] = (1+tmp[0],tmp[1])
      continue
    for j in range(i,min(m+1,i+9)):
      d = int(s[i:j+1])
      if d >= n: break
      tmp = dp[j+1]
      dp[i] = minn(dp[i],(1+tmp[0],d*power[tmp[0]]+tmp[1]))
  print(dp[1][1])

main()

