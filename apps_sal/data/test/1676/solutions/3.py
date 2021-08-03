import collections


class TaskMgr:
    def __init__(self, n, b):
        self.b = b
        self.lock_until = 1
        self.q = collections.deque()
        self.end = [-1 for i in range(n)]

    def empty(self):
        return len(self.q) == 0

    def full(self):
        return len(self.q) == self.b

    def add(self, i, t, d):
        if self.full():
            return
        self.q.append((i, t, d))

    def tick(self, now=None):
        if self.empty():
            return
        lock = self.lock_until
        now = now or lock
        if now < lock:
            return
        now = min(lock, now)
        i, t, d = self.q.popleft()
        t = max(t, now)
        end = t + d
        self.lock_until = end
        self.end[i] = end


def __starting_point():
    n, b = [int(x) for x in input().split()]
    mgr = TaskMgr(n, b)
    for i in range(n):
        t, d = [int(x) for x in input().split()]
        mgr.tick(t)
        mgr.add(i, t, d)
    while not mgr.empty():
        mgr.tick()
    print(' '.join(str(x) for x in mgr.end))


__starting_point()
