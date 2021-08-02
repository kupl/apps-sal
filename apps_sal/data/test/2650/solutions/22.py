import heapq

ymax = 200000
N, Q = list(map(int, input().split()))

yo = [[] for i in range(ymax + 1)]
ym = []
AB = [(0, 0)]
s = set()

for i in range(N):
    A, B = list(map(int, input().split()))
    AB.append((A, B))
    heapq.heappush(yo[B], (-A, i + 1))
    s.add(B)
for i in s:
    mA, c = yo[i][0]
    heapq.heappush(ym, (-mA, c, i))
for i in range(Q):
    C, D = list(map(int, input().split()))
    A, B = AB[C]
    AB[C] = (A, D)

    if yo[B][0][1] == C:
        while (yo[B]) and (AB[yo[B][0][1]][1] != B):
            heapq.heappop(yo[B])
        if yo[B]:
            mA, c = yo[B][0]
            heapq.heappush(ym, (-mA, c, B))
    heapq.heappush(yo[D], (-A, C))
    mA, c = yo[D][0]
    if c == C:
        heapq.heappush(ym, (-mA, c, D))

    while ym:
        if AB[ym[0][1]][1] != ym[0][2]:
            heapq.heappop(ym)
        elif ym[0][1] != yo[ym[0][2]][0][1]:
            heapq.heappop(ym)
        else:
            break
    print((ym[0][0]))
