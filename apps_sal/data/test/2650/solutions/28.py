import heapq as hq


class Delheap:

    def __init__(self):
        self.heap = []
        self.deleted = {}

    def __repr__(self):
        return str(self.heap)

    def push(self, x):
        hq.heappush(self.heap, x)

    def pop(self):
        while self.heap:
            x = hq.heappop(self.heap)
            if x in self.deleted and self.deleted[x] > 0:
                self.deleted[x] -= 1
                if self.deleted[x] == 0:
                    del self.deleted[x]
                continue
            return x
        return None

    def delete(self, x):
        if x not in self.deleted:
            self.deleted[x] = 1
        else:
            self.deleted[x] += 1

    def peek(self):
        x = self.pop()
        if x != None:
            self.push(x)
        return x


def __starting_point():
    (N, Q) = map(int, input().split())
    shozoku = []
    rate = []
    saikyo = Delheap()
    nurs = [Delheap() for _ in range(2 * 10 ** 5)]
    for _ in range(N):
        (a, b) = map(int, input().split())
        b -= 1
        shozoku.append(b)
        rate.append(a)
        nurs[b].push(-a)
    for i in range(2 * 10 ** 5):
        x = nurs[i].peek()
        if x != None:
            saikyo.push(-x)
    anss = []
    for _ in range(Q):
        (c, d) = map(int, input().split())
        c -= 1
        d -= 1
        nur = shozoku[c]
        saikyo.delete(-nurs[nur].peek())
        nurs[nur].delete(-rate[c])
        t = nurs[nur].peek()
        if t != None:
            saikyo.push(-t)
        shozoku[c] = d
        t = nurs[d].peek()
        if t != None:
            saikyo.delete(-t)
        nurs[d].push(-rate[c])
        saikyo.push(-nurs[d].peek())
        anss.append(saikyo.peek())
    print(*anss, sep='\n')


__starting_point()
