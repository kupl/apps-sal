from heapq import *
import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


dij = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def main():
    sa = sb = 0
    hp1 = []
    hp2 = []
    m = None
    for _ in range(II()):
        ab = input().split()
        if ab[0] == "1":
            a, b = int(ab[1]), int(ab[2])
            sb += b
            heappush(hp1, -a)
            heappush(hp2, a)
            while -hp1[0] > hp2[0]:
                heappush(hp1, -heappop(hp2))
                heappush(hp2, -heappop(hp1))
            if m == None:
                m = a
                continue
            if -hp1[0] > m:
                d = -hp1[0] - m
                sa += (len(hp1) - 1) // 2 * d - (len(hp2) + 1) // 2 * d
            if -hp1[0] < m:
                d = hp1[0] + m
                sa += -(len(hp1)) // 2 * d + (len(hp2)) // 2 * d
            sa += abs(m - a)
            m = -hp1[0]
        else:
            print(m, sa + sb)


main()
