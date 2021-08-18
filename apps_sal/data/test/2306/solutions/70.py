import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
def input(): return sys.stdin.readline().strip()
def NI(): return int(input())
def NMI(): return map(int, input().split())
def NLI(): return list(NMI())
def SI(): return input()


def make_cumulative(A):
    C = [0] * (len(A) + 1)
    for i, a in enumerate(A):
        i += 1
        C[i] = C[i - 1] + a
    return C


def main():
    N = NI()
    T = [0] + NLI()
    V = [0] + NLI() + [0]
    B = [[] for _ in range(N + 1)]
    cum_T = make_cumulative(T)[1:]

    limits = [[] for _ in range(N)]
    for i, v in enumerate(V):
        for t in range(N):
            if t == i - 1:
                limits[t].append([v, 0])
            elif t == i:
                limits[t].append([v, 1])
            elif t < i - 1:
                limits[t].append([v + (cum_T[i - 1] - cum_T[t]), -1])
            else:
                limits[t].append([v + (cum_T[t] - cum_T[i]), 1])
    limits = [sorted(l) for l in limits]

    ans = 0
    for li, limit in enumerate(limits):
        if limit[0][1] == -1:
            ans += limit[0][0] * T[li + 1] - T[li + 1]**2 / 2
            continue

        if limit[0][1] == 0:
            next_l = limit[1]
            for j in range(1, len(limit)):
                if limit[j][1] == -1:
                    next_l = limit[j]
                    break
            if next_l[1] == -1 and next_l[0] < limit[0][0] + T[li + 1]:
                ans += limit[0][0] * T[li + 1] - (limit[0][0] - next_l[0] + T[li + 1])**2 / 2
            else:
                ans += limit[0][0] * T[li + 1]
            continue

        stay = [l for l in limit if l[1] == 0]
        down = [l for l in limit if l[1] == -1]
        if down == []:
            down_l = [10**5, -1]
        else:
            down_l = down[0]
        if stay == []:
            stay_l = [10**5, 0]
        else:
            stay_l = stay[0]

        if down_l[0] >= limit[0][0] + T[li + 1] * 2:
            ans += limit[0][0] * T[li + 1] + T[li + 1] ** 2 / 2
            if limit[0][0] < stay_l[0] < limit[0][0] + T[li + 1]:
                ans -= (limit[0][0] + T[li + 1] - stay_l[0])**2 / 2
        else:
            h = (down_l[0] - limit[0][0]) / 2
            if stay_l[0] >= limit[0][0] + h:
                ans += (limit[0][0] + h) * T[li + 1] - h**2 / 2 - (T[li + 1] - h)**2 / 2
                continue

            m, M = min(limit[0][0], down_l[0] - T[li + 1]), max(limit[0][0], down_l[0] - T[li + 1])
            if M < stay_l[0] < limit[0][0] + h:
                ans += (limit[0][0] + h) * T[li + 1] - h ** 2 / 2 - (T[li + 1] - h) ** 2 / 2
                ans -= (limit[0][0] + h - stay_l[0]) ** 2
                continue

            if stay_l[0] <= M:
                ans += stay_l[0] * T[li + 1] - (stay_l[0] - limit[0][0])**2 / 2
                continue

    print(ans)


def __starting_point():
    main()


__starting_point()
