
"""

2^4通り -> 16

AB = A & AA = A なら1通り
AB = B & BB = B なら1通り

AB = A の時だけ考えればあとは反転
AA = B の時だけ考えればいい

BA = Aなら簡単
BA = BだとBBが連続できる


"""

import sys
from sys import stdin

mod = 10**9+7
N = int(input())
aa = input()
ab = input()
ba = input()
bb = input()

dp = [1,0]
for i in range(N-3):
    ndp = [0,0]
    ndp[0] = (dp[0] + dp[1]) % mod
    ndp[1] = dp[0]
    dp = ndp
ANSC = sum(dp) % mod

if N == 2:
    print((1))
    return

if ab == "A":

    if aa == "A":
        print((1))
        return
    else:

        if ba == "B":
            print((pow(2,N-3,mod)))
            return
        else:
            print (ANSC)
            return

else:

    if bb == "B":
        print((1))
        return

    else:
        if ba == "A":
            print((pow(2,N-3,mod)))
            return
        else:
            print (ANSC)
            return

