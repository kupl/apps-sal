import math
import collections
import itertools


def resolve():

    N = int(input())

    ans = 0
    for i in range(1, N + 1):
        if(10 <= i <= 99 or 1000 <= i <= 9999 or 100000 <= i <= 999999):
            continue
        ans += 1
    print(ans)


resolve()
