import heapq
q = int(input())
L = []
R = []
heapq.heapify(L)
heapq.heapify(R)
fx = 0
for i in range(q):
    Q = list(map(int, input().split()))
    if Q[0] == 1:
        (a, b) = (Q[1], Q[2])
        heapq.heappush(L, -a)
        heapq.heappush(R, a)
        l = -heapq.heappop(L)
        r = heapq.heappop(R)
        if l == a and r == a:
            heapq.heappush(L, -l)
            heapq.heappush(R, r)
        else:
            fx += abs(r - l)
            heapq.heappush(L, -r)
            heapq.heappush(R, l)
        x = -L[0]
        fx += b
    else:
        print(x, fx)
