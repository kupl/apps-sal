

from collections import defaultdict


N, P = map(int, input().split())
S = input()

"""
S[l:r]  : (S[l:] - S[r:]) / 10**x

Pが2,5以外であれば、S[l:]とS[r:]がPで割り切れればよい
2,5は10**xと互いに素ではないので例外。

例２の 2020について、左から4つ目の0に着目すると、
0
20
020
2020
いずれも2で割り切れるので、右端にくるものが２で割り切れるだけでよい。
"""

ans = 0

if P in [2, 5]:
    for i in range(N):
        if int(S[i]) % P == 0:
            ans += i + 1


else:
    mod_P = defaultdict(int)
    mod_P[0] += 1
    tmp = 0

    for i in range(N):
        tmp = int(S[N - 1 - i]) * pow(10, i, P) + tmp
        tmp %= P
        ans += mod_P[tmp]
        mod_P[tmp] += 1


print(ans)
