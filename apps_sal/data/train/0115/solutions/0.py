import random
import heapq
import sys


class BIT:

    def __init__(self, n):
        self.BIT = [0] * (n + 1)
        self.num = n

    def query(self, idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx & -idx
        return res_sum

    def update(self, idx, x):
        while idx <= self.num:
            self.BIT[idx] += x
            idx += idx & -idx
        return


input = sys.stdin.readline
n = int(input())
spell = [tuple(map(int, input().split())) for i in range(n)]
S = set([])
for i in range(n):
    S.add(abs(spell[i][1]))
S = list(S)
S.sort(reverse=True)
comp = {i: e + 1 for (e, i) in enumerate(S)}
N = len(S)
x_exist = BIT(N)
y_exist = BIT(N)
power = BIT(N)
(X, Y, S) = (0, 0, 0)
Xmax = []
Ymin = []
x_data = [0] * (N + 1)
y_data = [0] * (N + 1)
for i in range(n):
    (t, d) = spell[i]
    S += d
    if d < 0:
        id = comp[-d]
        if t == 0:
            X -= 1
            x_exist.update(id, -1)
            power.update(id, d)
            x_data[id] -= 1
        else:
            Y -= 1
            y_exist.update(id, -1)
            power.update(id, d)
            y_data[id] -= 1
    else:
        id = comp[d]
        if t == 0:
            X += 1
            x_exist.update(id, 1)
            power.update(id, d)
            heapq.heappush(Xmax, -d)
            x_data[id] += 1
        else:
            Y += 1
            y_exist.update(id, 1)
            power.update(id, d)
            heapq.heappush(Ymin, d)
            y_data[id] += 1
    if X == 0:
        if Y == 0:
            print(0)
        else:
            while not y_data[comp[Ymin[0]]]:
                heapq.heappop(Ymin)
            print(2 * S - Ymin[0])
    elif Y == 0:
        print(S)
    else:
        start = 0
        end = N
        while end - start > 1:
            test = (end + start) // 2
            if x_exist.query(test) + y_exist.query(test) <= Y:
                start = test
            else:
                end = test
        if y_exist.query(start) != Y:
            print(S + power.query(start))
        else:
            while not y_data[comp[Ymin[0]]]:
                heapq.heappop(Ymin)
            while not x_data[comp[-Xmax[0]]]:
                heapq.heappop(Xmax)
            print(S + power.query(start) - Ymin[0] - Xmax[0])
