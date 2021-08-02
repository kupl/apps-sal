from collections import defaultdict as dd
import math
import sys
input = sys.stdin.readline


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


q = nn()

for _ in range(q):
    n, m = mi()

    mat = []
    for i in range(n):
        row = lm()
        mat.append(row)
    zeros = [0] * (n + m - 1)
    ones = [0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                ones[i + j] += 1
            else:
                zeros[i + j] += 1
    ops = 0
    #print(ones, zeros)
    for i in range((m + n - 1) // 2):
        ops += min(zeros[i] + zeros[-i - 1], ones[i] + ones[-i - 1])

    print(ops)
