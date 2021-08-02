import sys
import numpy as np
input = sys.stdin.readline

_n, _t = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(_n)]
AB.sort()

ans = 0
table = np.zeros(_t, int)
for a, b in AB:
    ans = max(ans, max(table) + b)
    np.maximum(table[:-a] + b, table[a:], out=table[a:])


print(ans)
