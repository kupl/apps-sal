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
    for t in range(int(input())):
        impo = False
        n = int(input())
        users = input().split()
        users_set = set(users)
        users.insert(0, '0')
        m = int(input())
        msg = [None] * (m + 5)
        for i in range(1, m + 1):
            (user, text) = input().split(':')
            alts = set()
            if user != '?':
                user = users.index(user)
            else:
                for alt in users_set - {x for x in re.split('[^A-Za-z0-9]+', text)}:
                    alts.add(users.index(alt))
            msg[i] = dict(user=user, text=text, users=alts)
        for i in range(1, m + 1):
            if 1 <= i - 1:
                msg[i]['users'].discard(msg[i - 1]['user'])
            if i + 1 <= m:
                msg[i]['users'].discard(msg[i + 1]['user'])
            if msg[i]['user'] == '?' and len(msg[i]['users']) == 0:
                impo = True
                break
        if impo:
            print('Impossible')
            continue
        dp = [[0 for j in range(n + 5)] for i in range(m + 5)]
        for i in range(n + 5):
            dp[m + 1][i] = oo
        for i in range(m, 0, -1):
            u = msg[i]['user']
            for j in range(n + 1):
                if u != '?':
                    if u != j and dp[i + 1][u]:
                        dp[i][j] = u
                else:
                    for alt in msg[i]['users']:
                        if alt != j and dp[i + 1][alt]:
                            dp[i][j] = alt
                            break
        if not dp[1][0]:
            print('Impossible')
            continue
        j = 0
        for i in range(1, m + 1):
            print(users[dp[i][j]] + ':' + msg[i]['text'])
            j = dp[i][j]


main()
