from heapq import heappush, heappop
from random import randint
from time import time


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def push(self, value):
        heappush(self.queue, value)

    def pop(self):
        return heappop(self.queue)

    def __len__(self):
        return len(self.queue)

    def __contains__(self, item):
        return item in self.queue


n, m = map(int, input().split())
v = list(map(int, input().split()))

ans = 0

# 取得する操作を何回行うか？
for i in range(0, m + 1):

    # 操作残り回数
    lef = m - i

    hp = PriorityQueue()
    # 左側からどれだけ取るか？
    for j in range(0, i + 1):
        if j > n:
            break

        # 左側からj個取る
        for k in range(0, j):
            hp.push(v[k])

        # 右側から i-j個取る
        for k in range(0, i - j):
            if n - 1 - k < j:
                break
            hp.push(v[n - 1 - k])

        # minusは戻す
        for k in range(0, lef):
            if len(hp) == 0:
                break
            top = hp.pop()
            if top >= 0:
                hp.push(top)
                break

        ss = 0
        while len(hp) > 0:
            ss += hp.pop()

        ans = max(ans, ss)

print(ans)
