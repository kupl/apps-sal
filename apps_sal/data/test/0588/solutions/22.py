import math
import sys
sys.setrecursionlimit(10 ** 7)


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]


def LF():
    return [float(x) for x in sys.stdin.readline().split()]


def LS():
    return sys.stdin.readline().split()


def II():
    return int(sys.stdin.readline())


def SI():
    return sys.stdin.readline().strip()


INF = 10 ** 18
MOD = 10 ** 9 + 7


def main():
    N = II()
    engines = []
    for _ in range(N):
        (x, y) = LI()
        angle = math.atan2(y, x)
        engines.append((x, y, angle))
    engines.sort(key=lambda x: x[2])
    dist_max = 0
    cnt = -1
    for (x1, y1, angle1) in engines:
        cnt += 1
        if angle1 <= 0:

            def search_criteria(x):
                return True if angle1 <= x < angle1 + math.pi else False
        else:

            def search_criteria(x):
                return True if angle1 <= x or x < angle1 - math.pi else False
        x_sum = 0
        y_sum = 0
        for (x, y, angle) in engines[cnt:] + engines[:cnt]:
            if search_criteria(angle):
                x_sum += x
                y_sum += y
            dist_max = max(dist_max, math.sqrt(x_sum ** 2 + y_sum ** 2))
    print(dist_max)


main()
