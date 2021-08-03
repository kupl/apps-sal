import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
def input(): return sys.stdin.readline().strip()
def NI(): return int(input())
def NMI(): return map(int, input().split())
def NLI(): return list(NMI())
def SI(): return input()


def main():
    D, G = NMI()
    pc = [NLI() for _ in range(D)]
    ans = 1000

    bit_len = D
    for i in range(2**bit_len):
        ls = [0 for _ in range(bit_len)]
        for j in range(bit_len):
            if (i >> j) & 1:
                ls[j] = 1

        point = 0
        solved = 0
        half_way = ""

        for n in range(D):
            if ls[n] == 1:
                solved += pc[n][0]
                point += pc[n][0] * 100 * (n + 1) + pc[n][1]
            else:
                half_way = n

        if G > point:
            if half_way != "":
                remain = int(math.ceil((G - point) / ((half_way + 1) * 100)))
                if remain < pc[half_way][0]:
                    solved += remain
                    ans = min(ans, solved)
        else:
            ans = min(ans, solved)

    print(ans)


def __starting_point():
    main()


__starting_point()
