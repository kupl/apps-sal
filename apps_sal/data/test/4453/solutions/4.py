import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline


def listin():
    return list(map(int, input().split()))


def mapin():
    return map(int, input().split())


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1
    col = [0 for i in range(n)]
    c = 1
    for i in range(n):
        if not col[i]:
            s = i
            while col[s] == 0:
                col[s] = c
                s = a[s]
            c += 1
    d = defaultdict(int)
    for i in col:
        d[i] += 1
    ans = [0 for i in range(n)]
    for i in range(n):
        ans[i] = d[col[i]]
    print(*ans)
