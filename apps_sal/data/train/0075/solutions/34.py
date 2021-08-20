import math
(MIN_INF, MAX_INF) = (float('-inf'), float('inf'))


def get_len(n, R, alpha, beta):
    (maxx, maxy) = (MIN_INF, MIN_INF)
    (minx, miny) = (MAX_INF, MAX_INF)
    d = MAX_INF
    for i in range(n):
        theta = alpha * i + beta
        x = math.cos(theta) * R
        y = math.sin(theta) * R
        maxx = max(x, maxx)
        maxy = max(y, maxy)
        minx = min(x, minx)
        miny = min(y, miny)
    d = min(d, max(abs(maxx - minx), abs(maxy - miny)))
    return d


def main():
    T = int(input())
    for t in range(T):
        n = int(input()) * 2
        alpha = 2 * math.pi / n
        R = 1.0 / 2.0 / math.sin(math.pi / n)
        print(get_len(n, R, alpha, alpha / 4))


main()
