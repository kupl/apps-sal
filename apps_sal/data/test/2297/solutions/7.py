import sys
input = sys.stdin.readline
Q = int(input())
LR = [list(map(int, input().split())) for i in range(Q)]


def SUM(i):
    plus = i // 2
    minus = (i + 1) // 2
    P = (2 + 2 * plus) * plus // 2
    M = (1 + 2 * minus - 1) * minus // 2
    return P - M


for (l, r) in LR:
    print(SUM(r) - SUM(l - 1))
