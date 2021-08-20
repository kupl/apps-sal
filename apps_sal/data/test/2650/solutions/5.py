from heapq import heapify, heappop, heappush
(N, Q) = map(int, input().split())
where = []
rating = []
garten = [[] for _ in range(2 * 10 ** 5)]
saikyo = []
for i in range(N):
    (A, B) = map(int, input().split())
    where.append(B - 1)
    rating.append(A)
    heappush(garten[B - 1], (-A, i))
for i in range(2 * 10 ** 5):
    if not garten[i]:
        continue
    (rate, num) = garten[i][0]
    heappush(saikyo, (-rate, i))
for _ in range(Q):
    (C, D) = map(int, input().split())
    (C, D) = (C - 1, D - 1)
    moto = where[C]
    where[C] = D
    heappush(garten[D], (-rating[C], C))
    if garten[D][0][1] == C:
        heappush(saikyo, (rating[C], D))
    while garten[moto]:
        (a, b) = garten[moto][0]
        if where[b] == moto:
            break
        heappop(garten[moto])
    heappush(saikyo, (-a, moto))
    while True:
        (a, b) = saikyo[0]
        if not garten[b]:
            heappop(saikyo)
            continue
        if garten[b][0][0] == -a:
            break
        heappop(saikyo)
    print(a)
