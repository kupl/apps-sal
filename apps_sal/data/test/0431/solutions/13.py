#!/usr/bin/env python3
import sys
from operator import itemgetter


def explore_floor(floor, light, from_, to, is_last_floor):
    """from_, to is one of 'l' or 'r'"""
    if from_ != to:
        return len(floor) - 1
    else:
        if light == 0:
            return 0
        else:
            mul = 1 if is_last_floor else 2
            if from_ == 'l':
                indx = floor.rindex('1')
                return indx * mul
            else:
                indx = floor.index('1')
                return (len(floor) - indx - 1) * mul


def run_dp(n, m, floors, lights):
    dp_table = [[10 ** 10] * (n + 1) for __ in range(4)]
    dp_table[0][0] = -1
    dp_table[1][0] = 10 ** 10
    dp_table[2][0] = 10 ** 10
    dp_table[3][0] = 10 ** 10
    for indx in range(n):
        dp_table[0][indx + 1] = min(dp_table[2][indx], dp_table[0][indx]) + explore_floor(floors[indx], lights[indx], 'l', 'l', indx == n - 1) + 1
        dp_table[1][indx + 1] = min(dp_table[2][indx], dp_table[0][indx]) + explore_floor(floors[indx], lights[indx], 'l', 'r', indx == n - 1) + 1
        dp_table[2][indx + 1] = min(dp_table[1][indx], dp_table[3][indx]) + explore_floor(floors[indx], lights[indx], 'r', 'l', indx == n - 1) + 1
        dp_table[3][indx + 1] = min(dp_table[1][indx], dp_table[3][indx]) + explore_floor(floors[indx], lights[indx], 'r', 'r', indx == n - 1) + 1
    return dp_table


def get_virtual_max_floor(lights):
    n = len(lights)
    cnt = 0
    for val in reversed(list([elem == 0 for elem in lights])):
        if val:
            cnt += 1
        else:
            break
    return n - cnt


def main():
    n, m = list(map(int, sys.stdin.readline().split()))
    inp = sys.stdin.read().rstrip()
    floors = list(reversed(inp.split("\n")))
    assert len(floors) == n
    lights = list([sum(map(int, floor)) for floor in floors])
    assert len(lights) == n
    virtual_n = get_virtual_max_floor(lights)
    # sys.stderr.write("{}\n".format(lights))
    # sys.stderr.write("{}\n".format(virtual_n))
    if virtual_n == 0:
        print(0)
        return
    dp_table = run_dp(virtual_n, m, floors, lights)
    # sys.stderr.write("{}\n".format(dp_table))
    print(min([dp_table[indx][virtual_n] for indx in range(4)]))


def __starting_point():
    main()


__starting_point()
