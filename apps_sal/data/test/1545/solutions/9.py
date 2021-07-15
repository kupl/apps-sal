import sys
from collections import deque

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def get_minsp(message, As):
    min_sp = 1
    cur_len = 0
    capa = 0

    for ch in message:
        index = ord(ch) - ord('a')

        if cur_len == 0:
            cur_len += 1
            capa = As[index]
        else:
            capa = min(capa, As[index])

            if cur_len + 1 <= capa:
                cur_len += 1
            else:
                min_sp += 1
                cur_len = 1
                capa = As[index]

    return min_sp

def solve():
    MOD = 10**9 + 7
    n = int(input())
    msg = input()
    As = [int(i) for i in input().split()]
    caps = []

    for ch in msg:
        idx = ord(ch) - ord('a')
        caps.append(As[idx])

    dp = [0] * (n + 1)
    dp[0] = 1
    max_len = 0
    lim = 0

    for i in range(1, n + 1):
        lim = caps[i - 1]
        cur_len = 1
        for j in range(i - 1, -1, -1):
            if cur_len > lim:
                break

            max_len = max(max_len, cur_len)
            dp[i] += dp[j]
            dp[i] %= MOD
            lim = min(lim, caps[j - 1])
            cur_len += 1

    min_sp = get_minsp(msg, As)

    # debug(dp, locals())
    print(dp[n])
    print(max_len)
    print(min_sp)



def __starting_point():
    solve()
__starting_point()
