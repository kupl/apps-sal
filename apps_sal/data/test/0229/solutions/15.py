from collections import defaultdict
import sys
import os
import math


def __starting_point():
    n = int(input())
    arr = list(map(int, input().split()))
    temp = []
    for num in arr:
        if num not in temp:
            temp.append(num)
        if len(temp) > 3:
            print("NO")
            return
    temp.sort()
    if len(temp) < 3 or temp[0] + temp[2] == 2 * temp[1]:
        print("YES")
    else:
        print("NO")


__starting_point()
