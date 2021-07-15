3

# BEGIN template
import sys
import re
import pprint

def dbg(x,y=''):
  if len(y) > 0: y += ' = '
  sys.stderr.write('\n>>> '+y+pprint.pformat(x)+'\n')

oo = 0x3f3f3f3f3f3f3f3f
# END template

def main():
  for t in range(int(input())):
    # input
    n = int(input())
    users = input().split()
    users_set = set(users)
    users.insert(0,'0')
    m = int(input())
    msg = [None]*(m+5)
    for i in range(1,m+1):
      user, text = input().split(':')
      alts = set()
      if user != '?':
        user = users.index(user)
        alts.add(user)
      else:
        # this shit is pretty fucked up, dude
        for alt in users_set - {x for x in re.split('[^A-Za-z0-9]+',text)}:
          alts.add(users.index(alt))
      msg[i] = dict(user=user, text=text, users=alts)
    # remove before and after
    for i in range(1,m+1):
      if 1 <= i-1:  msg[i]['users'].discard(msg[i-1]['user'])
      if i+1 <= m:  msg[i]['users'].discard(msg[i+1]['user'])
    # compute answer
    dp = [[0 for j in range(n+5)] for i in range(m+5)]
    for i in range(n+5):
      dp[m+1][i] = oo
    for i in range(m,0,-1):
      for j in range(n+1):
        for k in msg[i]['users']:
          if k != j and dp[i+1][k]:
            dp[i][j] = k
            break
    # output
    if not dp[1][0]:
      print('Impossible')
      continue
    j = 0
    for i in range(1,m+1):
      print(users[dp[i][j]]+':'+msg[i]['text'])
      j = dp[i][j]

main()

