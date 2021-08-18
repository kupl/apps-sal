import heapq
Q = int(input())

left, right = [], []
Lsum, Rsum = 0, 0
Lcnt, Rcnt = 0, 0
B = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if len(q) == 1:
        l = (-1) * heapq.heappop(left)
        heapq.heappush(left, (-1) * l)
        print(l, Rsum // 2 - Lsum // 2 + B)
    else:
        _, a, b = q
        B += b
        heapq.heappush(left, (-1) * a)
        heapq.heappush(right, a)
        Lsum += a
        Lcnt += 1
        Rsum += a
        Rcnt += 1
        l = (-1) * heapq.heappop(left)
        r = heapq.heappop(right)
        if l >= r:
            Lsum = Lsum - l + r
            Rsum = Rsum - r + l
            l, r = r, l
        heapq.heappush(left, (-1) * l)
        heapq.heappush(right, r)
