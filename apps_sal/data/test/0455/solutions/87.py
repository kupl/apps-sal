import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


N = int(sys.stdin.buffer.readline())
XY = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(N)]

# マンハッタン距離の偶奇は全部同じじゃないとだめ
x, y = XY[0]
odd = (abs(x) + abs(y)) % 2
ok = True
for x, y in XY:
    ok &= (abs(x) + abs(y)) % 2 == odd

if not ok:
    print(-1)
    return


def solve(x):
    # a + b = 2^39 - 1
    # a - b = x
    # とおいて a を求める
    # 2a = 2^39 - 1 + x
    n = int((2 ** 39 - 1 + x) // 2)
    ret = []
    for _ in range(39):
        if n & 1:
            ret.append(1)
        else:
            ret.append(-1)
        n >>= 1
    ret = np.array(ret, dtype=int)
    return ret


P = [complex(x, y) for x, y in XY]
P = np.array(P)
# マンハッタン距離を奇数にする
# 原点を (-1, 0) だけずらす
if not odd:
    P -= 1
# 45度回転してみる
# アームの長さが決まってるとき、xとyについて独立にプラスマイナスを決められるようになる
P *= 1 + 1j

D = (2 ** np.arange(39, dtype=int)).tolist()
ans = []
for p in P:
    xd = solve(p.real)
    yd = solve(p.imag)
    W = np.empty_like(D, dtype='U1')
    W[(xd > 0) & (yd > 0)] = 'R'
    W[(xd > 0) & (yd < 0)] = 'D'
    W[(xd < 0) & (yd > 0)] = 'U'
    W[(xd < 0) & (yd < 0)] = 'L'
    ans.append(''.join(W))

if not odd:
    D.append(1)
    for i in range(len(ans)):
        ans[i] += 'R'
print(len(D))
print(*D)
print(*ans, sep='\n')

