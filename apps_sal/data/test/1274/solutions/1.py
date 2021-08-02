import sys
import heapq

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()

N, M = inl()


class MinHeap(object):
    def __init__(self):
        self.h = []

    def push(self, x):
        heapq.heappush(self.h, x)

    def pop(self):
        return heapq.heappop(self.h)

    def __getitem__(self, i):
        return self.h[i]

    def __len__(self):
        return len(self.h)

    def __bool__(self):
        return bool(self.h)


class MaxHeap(MinHeap):
    class Negator(object):
        def __init__(self, val):
            self.val = val

        def __lt__(self, other):
            return self.val > other.val

        def __eq__(self, other):
            return self.val == other.val

        def __str__(self):
            return str(self.val)

    def push(self, x):
        heapq.heappush(self.h, self.Negator(x))

    def pop(self):
        return heapq.heappop(self.h).val


def solve():
    jobs = []
    for i in range(N):
        a, b = inl()
        jobs.append((a, b))
    jobs.sort()

    hp = MaxHeap()
    ans = 0
    j = 0
    for d in range(1, M + 1):
        while j < N and jobs[j][0] == d:
            a, b = jobs[j]
            hp.push(b)
            j += 1
        if hp:
            ans += hp.pop()
    return ans


print((solve()))
