import itertools
import sys
input = sys.stdin.readline

"""
(a_i+1,a_{i+1}] に x がある間は...使う。傾き-1
a_{i+1} -> a_{i+1} + 1 のところでがくっと下がる
そこからa_iまでは傾き0
"""

N, M = map(int, input().split())
A = [int(x) for x in input().split()]
FROM = A[:-1]
TO = A[1:]

d_slope = [0] * (M + 1)

"""
5,4,3,2,1,5,5,5,5
0,-1,-1,-1,-1,4,0,0,0
0,-1,0,0,0,0,5,-4,0,0
"""

for x, y in zip(FROM, TO):
    if y < x:
        y += M
    z = y - x
    if z == 1:
        continue
    d_slope[1 + (x + 1) % M] += -1
    d_slope[1 + y % M] += z
    d_slope[1 + (y + 1) % M] += 1 - z

slope = list(itertools.accumulate(d_slope))
S = sum(slope)
slope = [x - S // M for x in slope]
slope[0] = 0

cnt = 0
for x, y in zip(FROM, TO):
    if x < y:
        cnt += (y - x)
    else:
        cnt += y

answer = cnt - slope[1] + min(itertools.accumulate(slope[1:]))
print(answer)
