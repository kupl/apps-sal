import sys
from heapq import heappop, heappush, heapify

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
MAX = 2 * 10 ** 5 + 1


def resolve():
    def max_rate_in_cls(c):
        q = class_rate[c]
        while q:
            x, enj = q[0]
            if enji_cls[enj] == c:
                return -x
            else:
                heappop(q)
        return 0

    def get_ans():
        q = max_rate
        while True:
            x, c = q[0]
            if max_rate_in_cls(c) == x:
                return x
            heappop(q)

    def max_rate_in_cls(c):
        q = class_rate[c]
        while q:
            x, enj = q[0]
            if enji_cls[enj] == c:
                return -x
            else:
                heappop(q)
        return 0

    n, q = list(map(int, input().split()))

    enji_rate = [0] * (n + 1)
    enji_cls = [0] * (n + 1)
    class_rate = [[] for _ in range(MAX)]
    for i in range(1, n + 1):
        rate, cls = list(map(int, input().split()))
        enji_rate[i] = rate
        enji_cls[i] = cls
        heappush(class_rate[cls], (-rate, i))

    max_rate = []
    for c in range(MAX):
        x = max_rate_in_cls(c)
        if x:
            max_rate.append((x, c))
    heapify(max_rate)

    for _ in range(q):
        enj, after_cls = list(map(int, input().split()))
        before_cls = enji_cls[enj]
        heappush(class_rate[after_cls], (-enji_rate[enj], enj))
        enji_cls[enj] = after_cls
        for c in (before_cls, after_cls):
            x = max_rate_in_cls(c)
            if x != 0:
                heappush(max_rate, (x, c))
        print((get_ans()))


def __starting_point():
    resolve()

__starting_point()
