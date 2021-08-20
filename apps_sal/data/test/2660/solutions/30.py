import heapq
Q = int(input())
m = L = R = 0
(l, r) = ([], [])
n = 0
b = 0
for i in range(Q):
    query = list(map(int, input().split()))
    if len(query) == 3:
        b += query[2]
        new = query[1]
        if n == 0:
            m = new
        elif n == 1:
            if new <= m:
                heapq.heappush(l, -new)
                heapq.heappush(r, m)
                (L, R) = (new, m)
                m = new
            else:
                heapq.heappush(l, -m)
                heapq.heappush(r, new)
                (L, R) = (m, new)
        elif n == 2:
            if new < m:
                m = -heapq.heappop(l)
                heapq.heappush(l, -new)
                L = new
            else:
                _r = heapq.heappop(r)
                if new < _r:
                    m = new
                    heapq.heappush(r, _r)
                else:
                    m = _r
                    heapq.heappush(r, new)
                    R = new
        else:
            _l = -l[0]
            _r = r[0]
            if n % 2:
                if new <= _l:
                    _ = heapq.heappop(l)
                    heapq.heappush(l, -new)
                    heapq.heappush(r, m)
                    (m, L, R) = (_l, L + new, R + m)
                elif new <= m:
                    heapq.heappush(r, m)
                    (m, L, R) = (new, L + new, R + m)
                else:
                    heapq.heappush(r, new)
                    (L, R) = (L + m, R + new)
            elif new <= m:
                heapq.heappush(l, -new)
                L += new - m
            elif new <= _r:
                heapq.heappush(l, -m)
                m = new
            else:
                _ = heapq.heappop(r)
                heapq.heappush(l, -m)
                heapq.heappush(r, new)
                (m, R) = (_r, R + new - _r)
        n += 1
    else:
        print(m, R - L + b)
