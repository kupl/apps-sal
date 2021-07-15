class HeapQueue:
    """
    q = HeapQueue()
    q.append(p, v)
    v = q.pop()
    """
    from heapq import heappop, heappush, heappushpop, heapreplace

    def __init__(self, reverse=False):
        self.reverse = reverse
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def append(self, p, v):
        self.heappush(self.heap, (-p if self.reverse else p, v))

    def appendpop(self, p, v):
        return self.heappushpop(self.heap, (-p if self.reverse else p, v))[1]

    def popappend(self, p, v):
        return self.heapreplace(self.heap, (-p if self.reverse else p, v))[1]

    def pop(self):
        return self.heappop(self.heap)[1]

    def front(self):
        return self.heap[0][1]


N = int(input())
A = [int(s) for s in input().split()]
S = []
T = []

S.append(sum(A[:N]))
q = HeapQueue()
for a in A[:N]:
    q.append(a, a)
for a in A[N:2*N]:
    m = q.appendpop(a, a)
    S.append(S[-1] + a - m)

T.append(sum(A[-N:]))
q = HeapQueue(reverse=True)
for a in A[-N:]:
    q.append(a, a)
for a in A[-N-1:N-1:-1]:
    m = q.appendpop(a, a)
    T.append(T[-1] + a - m)
ans = max([S[i] - T[N - i] for i in range(N + 1)])
print(ans)

