from collections import defaultdict, deque
import sys
import heapq
from bisect import bisect_left, bisect_right
import copy
import math


def getN():
    return int(input())


def getNM():
    return list(map(int, input().split()))


def getList():
    return list(map(int, input().split()))


def getZList():
    return [int(x) - 1 for x in input().split()]


input = sys.stdin.readline
# sys.setrecursionlimit(1000000)
INF = 10 ** 17
MOD = 1000000007


class LazyHeap():
    def __init__(self, init_arr=[]):
        self.heap = []
        self.lazy = defaultdict(int)
        self.len = 0
        for init_element in init_arr:
            heapq.heappush(self.heap, init_element)
            self.len += 1

    def __len__(self):
        return self.len

    def push(self, k):
        heapq.heappush(self.heap, k)
        self.len += 1

    def pop(self):
        self._clear()
        return heapq.heappop(self.heap)

    def get(self):
        self._clear()
        return self.heap[0]

    def _clear(self):
        while True:
            cand = self.heap[0]
            if cand in self.lazy and self.lazy[cand] > 0:
                heapq.heappop(self.heap)
                self.lazy[cand] -= 1

            else:
                return

    def remove(self, k):
        self.lazy[k] += 1
        self.len -= 1


N_KINDER = 200200
# N_KINDER = 2 * (10 ** 5) + 1
n, q = getList()
kinder = [LazyHeap() for i in range(N_KINDER)]
saikyo = LazyHeap()
saikyo_ref = []
pos_ref = [-1 for i in range(n)]
enji_ref = []

for i in range(n):
    a, b = getList()
    b -= 1
    enji_ref.append((-a, b))
    kinder[b].push(-a)

for kin in kinder:
    if kin:
        candidate = kin.get()
        saikyo.push(-candidate)
        saikyo_ref.append(candidate)
    else:
        saikyo_ref.append(0)

for i in range(q):
    c, d = getZList()
    mv_rate = enji_ref[c][0]
    prev = enji_ref[c][1]
    nxt = d
    pos_ref[c] = d
    enji_ref[c] = (mv_rate, d)
    # 移動元についての処理
    kinder[prev].remove(mv_rate)

    kp, kn = kinder[prev], kinder[nxt]
    if not kp:
        # 移動して園児0人になった場合
        saikyo_ref[prev] = 0
        saikyo.remove(-mv_rate)
    elif saikyo_ref[prev] != kp.get():
        saikyo.remove(-mv_rate)
        saikyo.push(-kp.get())
        saikyo_ref[prev] = kp.get()

    # 移動先についての処理
    kn.push(mv_rate)
    if mv_rate < saikyo_ref[nxt]:
        saikyo.remove(-saikyo_ref[nxt])
        saikyo.push(-mv_rate)
        saikyo_ref[nxt] = mv_rate

    print((saikyo.get()))
# print(rate)
