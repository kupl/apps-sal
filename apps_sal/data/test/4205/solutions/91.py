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
    p = list(map(int, input().split()))
    ans = False

    tmp = copy.deepcopy(p)
    isOK = True
    for k in range(N - 1):
        if(tmp[k] >= tmp[k + 1]):
            isOK = False
    if(isOK):
        ans = True

    for i in range(N):
        for j in range(i + 1, N):
            tmp = []
            tmp = copy.deepcopy(p)
            tmp[i], tmp[j] = tmp[j], tmp[i]
            isOK = True
            for k in range(N - 1):
                if(tmp[k] >= tmp[k + 1]):
                    isOK = False
            if(isOK):
                ans = True
    YesNo(ans)


resolve()
