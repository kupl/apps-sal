import sys
sys.setrecursionlimit(10**9)

N = int(input())
mod = 10**9 + 7
DP = dict()
DP[(0, 0)] = 1  # a+b,a^b
DP[(1, 0)] = 1
DP[(1, 1)] = 2


def ans(S, X):
    # print(S,X)
    if DP.get((S, X)) != None:
        return DP[(S, X)]
    if S == 0:
        return 1
    # if X>S:
    #    return ans(S,S)

    DP[(S, X)] = (ans(S // 2, X // 2) + ans((S - 1) // 2, (X - 1) // 2) + ans((S - 2) // 2, (X - 2) // 2)) % mod
    # 一番下の桁をみて、bitが0,0の場合,1,0の場合,1,1の場合.
    # 三つ目の場合は本来ans((S-2)//2,X//2)だが,今回扱うのはS=Xのときで,X>Sのときは0になるので,ans((S-2)//2,(X-2)//2)で良いはず.
    return DP[(S, X)]


print((ans(N, N)))
