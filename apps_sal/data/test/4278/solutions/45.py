import math
import collections
import itertools
import copy


def YesNo(Bool):
    if(Bool):
        print("YES")
    else:
        print("NO")
    return


def resolve():

    N = int(input())
    tmp = {}

    ans = 0
    for i in range(N):
        S = list(input())
        S.sort()
        Ssort = ''.join(S)
        if(Ssort in tmp):
            tmp[Ssort] += 1
        else:
            tmp[Ssort] = 1

    for i in list(tmp.values()):
        ans += (i * (i - 1)) // 2

    print(ans)


resolve()
