import math
import random
import time


def __starting_point():
    room = input().split(' ')
    b = input().split(' ')
    res = [0 for i in range(int(room[0]))]

    for i in range(int(room[1])):
        for num in range(int(b[i]) - 1, int(room[0])):
            if res[num] == 0:
                res[num] = int(b[i])

    for i in range(len(res)):
        print(repr(res[i]) + ' ', end="")


__starting_point()
