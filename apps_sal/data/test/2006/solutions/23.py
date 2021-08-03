import math


def solution():
    n, m = [int(x) for x in input().split(' ')]
    matrix = []
    s = []
    for i in range(n):
        line = list(input())
        matrix.append(line)
        coo = line.index('S') - line.index('G')
        if coo < 0:
            return -1
        s.append(coo)
    s = set(s)
    return len(s)


print(solution())
