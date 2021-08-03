from collections import defaultdict
import sys
import os
import math


def __starting_point():
    #n, m = list(map(int, input().split()))
    # sys.stdout.flush()
    n, c = list(map(int, input().split()))
    time = list(map(int, input().split()))
    ans = 1
    for i in range(1, n):
        if time[i] - time[i - 1] <= c:
            ans += 1
        else:
            ans = 1
    print(ans)


__starting_point()
