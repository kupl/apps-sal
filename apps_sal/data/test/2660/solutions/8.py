import heapq


class heap:

    def __init__(self):
        self.heap = []
        self.asum = 0


class solve:

    def __init__(self):
        self.lower = heap()
        self.upper = heap()
        self.bsum = 0
        self.amed = 0

    def update(self, a, b):
        self.bsum += b
        if a > self.amed:
            self.__add(self.upper, a)
        else:
            self.__add(self.lower, -a)
        if len(self.upper.heap) > len(self.lower.heap):
            a = self.__del(self.upper)
            self.__add(self.lower, -a)
        elif len(self.lower.heap) > len(self.upper.heap) + 1:
            a = self.__del(self.lower)
            self.__add(self.upper, -a)
        self.amed = -self.lower.heap[0]

    def get_min(self):
        x = self.amed
        fx = x * len(self.lower.heap) + self.lower.asum + (self.upper.asum - x * len(self.upper.heap))
        fx += self.bsum
        print(x, fx)

    def __add(self, heap, a):
        heapq.heappush(heap.heap, a)
        heap.asum += a

    def __del(self, heap):
        a = heapq.heappop(heap.heap)
        heap.asum -= a
        return a


fx = solve()
Q = int(input())
for _ in range(Q):
    q = input()
    if q[0] == '2':
        fx.get_min()
    else:
        (_, a, b) = map(int, q.split())
        fx.update(a, b)
