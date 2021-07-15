# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.readline
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
from itertools import combinations

def run():
    N, K = map(int, sysread().split())
    niku = []
    for i in range(N):
        niku.append([i]+list(map(int, sysread().split())))

    high_t = math.sqrt(2000**2 + 2000**2) * 101
    low_t = 0
    current = (high_t + low_t) / 2
    delta = 5e-7
    if K == 1:
        print(0)
        return None

    while high_t - low_t > delta:
        done = False
        c = [(current / ci) ** 2 for _, _, _, ci in niku]
        for i, xi, yi, _ in niku:
            if done:
                break
            K0 = 0
            for k, xk, yk, _ in niku:
                if done:
                    break
                ck = c[k]
                if ((xi - xk) ** 2 + (yi - yk) ** 2) <= ck + delta:
                    K0 += 1
                if K0 >= K:
                    done = True


        for (i, xi, yi, _), (j, xj, yj, _) in combinations(niku, 2):
            if done:
                break
            ci, cj = c[i], c[j]
            xj -= xi
            yj -= yi
            d2 = xj ** 2 + yj ** 2
            d = math.sqrt(d2)

            x = (d2 + ci - cj) / (2 * d)
            e = ci - x ** 2
            if e < 0 or math.sqrt(ci) + math.sqrt(cj) < d:
                continue
            else:
                e = math.sqrt(e)

            vx1, vy1 = xj / d, yj / d
            vx2, vy2 = yj / d, -xj / d

            X1 = vx1 * x + vx2 * e + xi
            X2 = vx1 * x - vx2 * e + xi
            Y1 = vy1 * x + vy2 * e + yi
            Y2 = vy1 * x - vy2 * e + yi

            K1 = 0
            K2 = 0

            for k, xk, yk, _ in niku:
                if done:
                    break
                ck = c[k]
                if ((xk - X1) ** 2 + (yk - Y1) ** 2) <= ck + delta:
                    K1 += 1
                if ((xk - X2) ** 2 + (yk - Y2) ** 2) <= ck + delta:
                    K2 += 1
                if K1 >= K or K2 >= K:
                    done = True


        if done:
            high_t = current
            current = (high_t + low_t) / 2
        else:
            low_t = current
            current = (high_t + low_t) / 2

    print((low_t + high_t) / 2)
    return None

def __starting_point():
    run()
__starting_point()
