import heapq
Q = int(input())
qs = [tuple(map(int, input().split())) for i in range(Q)]


class Heapq:

    def __init__(self, arr, desc=False):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)

    def pop(self):
        return heapq.heappop(self.hq) * self.sign

    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)

    def top(self):
        return self.hq[0] * self.sign


lq = Heapq([], True)
rq = Heapq([])
ans = 0
for q in qs:
    if q[0] == 2:
        print(lq.top(), ans)
        continue
    (_, a, b) = q
    ans += b
    lq.push(a)
    rq.push(a)
    if lq.top() > rq.top():
        l = lq.pop()
        r = rq.pop()
        ans += abs(l - r)
        lq.push(r)
        rq.push(l)
