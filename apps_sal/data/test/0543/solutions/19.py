from collections import defaultdict
import sys
import os
import math


def __starting_point():
    #n, m = list(map(int, input().split()))
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr[i] % 2 != 0:
            if i == n - 1 or arr[i + 1] == 0:
                print("NO")
                return
            arr[i + 1] -= 1
    print("YES")


__starting_point()
