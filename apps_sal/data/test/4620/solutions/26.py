"""
Created on Fri Oct  2 01:57:07 2020

@author: liang
"""
import math

N = int(input())
Stations = list()
for i in range(N - 1):
    C, S, F = map(int, input().split())
    Stations.append((C, S, F))


def solve(n, time):
    if n == N - 1:
        return time
    C, S, F = Stations[n]
    tmp = max(S + C, math.ceil(time / F) * F + C)
    return solve(n + 1, tmp)


for i in range(N):
    print(solve(i, 0))
