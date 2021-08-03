import sys
import math
from collections import deque

input = sys.stdin.readline


def solve(n, x_y_list):
    radians = [(math.atan2(y, x), x, y) for x, y in x_y_list]
    radians.sort()
    radians = radians + radians

    max_square_distance = 0
    for start in range(n):
        sum_x = sum_y = 0
        for i in range(n):
            _, x, y = radians[start + i]
            sum_x += x
            sum_y += y
            square_distance = sum_x ** 2 + sum_y ** 2
            if max_square_distance < square_distance:
                max_square_distance = square_distance
    return math.sqrt(max_square_distance)


def __starting_point():
    n = int(input())
    x_y_list = [tuple(map(int, input().split())) for _ in range(n)]

    answer = solve(n, x_y_list)
    print(answer)


__starting_point()
