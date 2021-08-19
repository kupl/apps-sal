import sys


def solve():
    (end, full, real_mid, times) = map(int, sys.stdin.readline().split())
    oil = full
    cnt = 0
    for i in range(times):
        if i % 2 == 0:
            mid = real_mid
        else:
            mid = end - real_mid
        if mid > oil:
            return -1
        oil -= mid
        if i != times - 1:
            if (end - mid) * 2 > full:
                return -1
            if (end - mid) * 2 > oil:
                oil = full
                cnt += 1
        else:
            if end - mid > full:
                return -1
            if end - mid > oil:
                oil = full
                cnt += 1
        oil -= end - mid
    return cnt


print(solve())
