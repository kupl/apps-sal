import sys
import math
import itertools
import collections
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD2 = 998244353
INF = float('inf')
def input(): return sys.stdin.readline().strip()


def NI(): return int(input())
def NMI(): return map(int, input().split())
def NLI(): return list(NMI())
def SI(): return input()


def main():
    S = SI()
    Q = NI()

    que = deque(list(S))

    reverse = False

    for q in range(Q):
        query = input()

        if query == "1":
            if reverse == False:
                reverse = True
            else:
                reverse = False
        else:
            x, y, z = map(str, query.split())
            if reverse == False:
                if y == "1":
                    que.appendleft(z)
                else:
                    que.append(z)
            else:
                if y == "1":
                    que.append(z)
                else:
                    que.appendleft(z)

    if reverse == True:
        print("".join(reversed(list(que))))
    else:
        print("".join(list(que)))


def __starting_point():
    main()


__starting_point()
