__author__ = 'MoonBall'

import sys
# sys.stdin = open('data/D.in', 'r')
T = 1

def process():
    ans = []
    N = int(input())
    for i in range(1, N + 1):
        a = N + i * (i - 1) * (i + 1) // 6
        j, mod = divmod(a, i * (i + 1) // 2)
        if i > j: break
        if mod: continue
        ans.append((i, j))
        if i != j: ans.append((j, i))

    ans.sort()
    print(len(ans))
    for i, j in ans: print(i, j)





for _ in range(T):
    process()

