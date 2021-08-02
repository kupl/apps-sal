#--初期の並びを圧縮表示,逆立ち、正立を目印--#
import sys
import math
import collections
import itertools
input = sys.stdin.readline

N, K = list(map(int, input().split()))
S = input().rstrip()

stand = []
s_or_r = []

s_bf = '.'
cnt = 0
for i in range(N):
    if s_bf != S[i] and i != 0:
        stand.append(cnt)
        s_or_r.append(s_bf)
        cnt = 1
        s_bf = S[i]
    else:
        cnt += 1
        s_bf = S[i]
stand.append(cnt)
s_or_r.append(s_bf)


# --正立kまで許容して足す。maxが答え
if s_or_r.count('0') <= K:
    print((len(S)))
    return
#--成形==#
if s_or_r[0] == '0':
    s_or_r = ['1'] + s_or_r
    stand = [0] + stand
if s_or_r[-1] == '0':
    s_or_r.append('1')
    stand.append(0)
#初期条件#
tmp = sum(stand[0:2 * K + 1])
ans = tmp
for i in range(2, len(stand) - 2 * K, 2):
    tmp += -(stand[i - 1] + stand[i - 2]) + stand[i + 2 * K - 1] + stand[i + 2 * K]
    ans = max(ans, tmp)
print(ans)
