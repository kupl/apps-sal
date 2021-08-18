import heapq
from heapq import heappush as push_
from heapq import heappop as pop_


class heapT():
    def __init__(self, T):
        self.Q = []
        self.curT = 0
        self.maxT = T
        self.his = []

    def push(self, t, index):
        push_(self.Q, (-t, index))
        self.his.append(index)
        self.curT += t

        while self.curT > self.maxT:
            self.pop()

    def pop(self):
        t, ind = pop_(self.Q)
        self.his.append(ind)
        self.curT -= t * -1

    def normalize(self, length):
        while len(self.Q) > length:
            self.pop()


def solve(a, n, T):
    a = sorted(a, key=lambda x: x[0], reverse=True)
    H = heapT(T)

    max_ = -1
    pos = None

    for ak, t, ind in a:
        H.push(t, ind)
        H.normalize(ak)

        if len(H.Q) > max_:
            max_ = len(H.Q)
            pos = len(H.his)

    d = {}
    if pos is not None:
        for x in H.his[:pos]:
            if x not in d:
                d[x] = 1
            else:
                del d[x]

    if len(d) > 0:
        print(len(d))
        print(len(d))
        print(' '.join([str(x + 1) for x in d]))
    else:
        print('0' + '\n' + '0')


n, T = list(map(int, input().split()))
a = [list(map(int, input().split())) + [_] for _ in range(n)]
solve(a, n, T)
