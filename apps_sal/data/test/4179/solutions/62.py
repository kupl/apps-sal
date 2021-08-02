import sys
import numpy as np
input = sys.stdin.readline
N, M, C = list(map(int, input().split()))
B = np.array(list(map(int, input().split())))


def main():
    count = 0
    for i in range(N):
        A = np.array(list(map(int, input().split())))
        if sum(A * B) + C > 0:
            count += 1
    return count


def __starting_point():
    print((main()))


__starting_point()
