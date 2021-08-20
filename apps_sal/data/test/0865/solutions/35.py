import sys
import numpy as np
input = sys.stdin.readline
(_n, _t) = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(_n)]
AB.sort()


def dp(t, ablist):
    ans = 0
    table = np.zeros(t, int)
    for (a, b) in ablist:
        ans = max(ans, max(table) + b)
        np.maximum(table[:-a] + b, table[a:], out=table[a:])
    return ans


print(dp(_t, AB))
