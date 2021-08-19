#!/usr/local/bin/python3

import math


def power(P, X):
    ans = 0
    for x in X:
        ans += (x - P)**2
    return ans


N = int(input())
X = list(map(int, input().split()))
ave = sum(X) / N
candP = (math.ceil(ave), math.floor(ave))
power = min([power(P, X) for P in candP])

print(power)
