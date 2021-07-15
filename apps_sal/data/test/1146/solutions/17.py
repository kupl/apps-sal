__author__ = 'MoonBall'

import sys
# sys.stdin = open('data/A.in', 'r')
T = 1

def process():
    N, M = list(map(int, input().split()))
    f = [0] * (M + 1)
    for _ in range(N):
        a = list(map(int, input().split()))
        for i in range(a[0]): f[a[i + 1]] = 1

    print('YES' if sum(f) == M else 'NO')






for _ in range(T):
    process()

