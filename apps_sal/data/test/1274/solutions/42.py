import heapq


def INT(): return int(input())
def INTM(): return map(int, input().split())
def STRM(): return map(str, input().split())
def STR(): return str(input())
def LIST(): return list(map(int, input().split()))
def LISTS(): return list(map(str, input().split()))


def do():
    n, m = INTM()
    ptj = [[] for i in range(10**5)]
    ans = 0
    for i in range(n):
        a, b = INTM()
        a -= 1
        b *= (-1)
        ptj[a].append(b)
    h = []
    for i in range(m):
        for p in ptj[i]:
            heapq.heappush(h, p)
        if len(h) != 0:
            ans += heapq.heappop(h)
    print(0 - ans)


def __starting_point():
    do()


__starting_point()
