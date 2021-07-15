# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

"""
Nが小さいので、Y座標でcandに入れておく
"""
N = ir()
AB = [lr() for _ in range(N)]
CD = [lr() for _ in range(N)]
cand = [0] * (2*N)
ABCD = [(a, b, 0) for a, b in AB] + [(c, d, 1) for c, d in CD]
ABCD.sort()
answer = 0
for X, Y, Z in ABCD:
    if Z == 0:
        cand[Y] += 1
    else:
        for y in range(Y-1, -1, -1):
            if cand[y] > 0:
                answer += 1
                cand[y] -= 1
                break

print(answer)

