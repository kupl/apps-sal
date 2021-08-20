import heapq
from collections import deque
import sys
INF = float('inf')


class MaxHeap(object):

    def __init__(self, x):
        self.heap = [-e for e in x]
        heapq.heapify(self.heap)

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        return -heapq.heappop(self.heap)


class MinHeap(object):

    def __init__(self, x):
        self.heap = [e for e in x]
        heapq.heapify(self.heap)

    def push(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        return heapq.heappop(self.heap)


def solve(N: int, a: 'List[int]'):
    mae = MinHeap(a[:N])
    mae_tot = [sum(a[:N])]
    for curr in range(N, 2 * N):
        mae.push(a[curr])
        mmin = mae.pop()
        mae_tot.append(mae_tot[-1] + a[curr] - mmin)
    ushiro = MaxHeap(a[2 * N:])
    ushiro_tot = [sum(a[2 * N:])]
    for curr in range(2 * N - 1, N - 1, -1):
        ushiro.push(a[curr])
        umax = ushiro.pop()
        ushiro_tot.append(ushiro_tot[-1] + a[curr] - umax)
    m = -INF
    for (mt, ut) in zip(mae_tot, reversed(ushiro_tot)):
        m = max(m, mt - ut)
    print(m)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    a = [int(next(tokens)) for _ in range(3 * N)]
    solve(N, a)


def __starting_point():
    main()


__starting_point()
