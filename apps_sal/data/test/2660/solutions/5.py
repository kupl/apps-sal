import heapq

q = int(input())

nchange = 0
ming, maxg = [], []
heapq.heapify(ming)
heapq.heapify(maxg)
a = 0
b = 0
for i in range(q):
    qi = input()
    if qi[0] == '1':
        _, ai, bi = map(int, qi.split())
        b += bi
        nchange += 1
        if nchange % 2 == 1:
            if nchange == 1:
                x = ai
                continue
            Smax = -heapq.heappop(ming)
            Dmin = heapq.heappop(maxg)
            if Smax <= ai and ai <= Dmin:
                heapq.heappush(ming, -Smax)
                heapq.heappush(maxg, Dmin)
                x = ai
            elif ai < Smax:
                heapq.heappush(ming, -ai)
                heapq.heappush(maxg, Dmin)
                x = Smax
                a += Smax - ai
            else:
                heapq.heappush(ming, -Smax)
                heapq.heappush(maxg, ai)
                x = Dmin
                a += ai - Dmin
        else:
            heapq.heappush(ming, -min(x, ai))
            heapq.heappush(maxg, max(x, ai))
            a += abs(x - ai)
            x = -heapq.heappop(ming)
            heapq.heappush(ming, -x)
    else:
        print(x, a + b)
