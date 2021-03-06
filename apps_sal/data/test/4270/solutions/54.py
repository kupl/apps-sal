import heapq


def INT():
    return int(input())


def INTM():
    return map(int, input().split())


def STRM():
    return map(str, input().split())


def STR():
    return str(input())


def LIST():
    return list(map(int, input().split()))


def LISTS():
    return list(map(str, input().split()))


def do():
    n = INT()
    v = LIST()
    heapq.heapify(v)
    for i in range(n - 1):
        a = heapq.heappop(v)
        b = heapq.heappop(v)
        heapq.heappush(v, (a + b) / 2)
    print(heapq.heappop(v))


def __starting_point():
    do()


__starting_point()
