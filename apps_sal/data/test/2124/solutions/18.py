import pprint
import re
import sys
3


def dbg(x, y=''):
    if len(y) > 0:
        y += ' = '
    sys.stderr.write('\n>>> ' + y + pprint.pformat(x) + '\n')


oo = 4557430888798830399


def main():
    t = int(input())
    for t in range(t):
        n = int(input())
        users = set(input().split())
        m = int(input())
        msg = []
        for i in range(m):
            (user, text) = input().split(':')
            alts = set()
            if user != '?':
                alts.add(user)
            else:
                alts = users - {x for x in re.split('[^A-Za-z0-9]+', text)}
            msg.append(dict(user=user, text=text, users=alts))
        for i in range(m - 1):
            if len(msg[i]['users']) == 1:
                msg[i + 1]['users'].difference_update(msg[i]['users'])
        for i in range(m - 1, 0, -1):
            if len(msg[i]['users']) == 1:
                msg[i - 1]['users'].difference_update(msg[i]['users'])
        last = ''
        impo = False
        for i in range(m):
            msg[i]['users'].discard(last)
            if len(msg[i]['users']) == 0:
                impo = True
                break
            last = next(iter(msg[i]['users']))
            msg[i]['user'] = last
        if impo:
            print('Impossible')
            continue
        for i in range(m):
            print(msg[i]['user'] + ':' + msg[i]['text'])
        "\n    dp = [[0 for j in range(n+5)] for i in range(m+5)]\n    for i in range(1,n+5):\n      dp[m+1][i] = oo\n    for i in range(m,0,-1):\n      for j in range(n+1):\n        for k in msg[i]['users']:\n          if k != j and dp[i+1][k]:\n            dp[i][j] = k\n            break\n    # output\n    if not dp[1][0]:\n      print('Impossible')\n      continue\n    j = 0\n    for i in range(1,m+1):\n      print(users[dp[i][j]]+':'+msg[i]['text'])\n      j = dp[i][j]"


main()
