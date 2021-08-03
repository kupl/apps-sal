import heapq
x, y, z, k = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

V = {(0, 0, 0)}
Q = [(-(A[0] + B[0] + C[0]), 0, 0, 0)]
heapq.heapify(Q)


def isIn(tup):
    return tup[0] < x and tup[1] < y and tup[2] < z


for i in range(k):
    now = heapq.heappop(Q)
    print(-now[0])
    nex = (now[1] + 1, now[2], now[3])
    if not nex in V and isIn(nex):
        V.add(nex)
        heapq.heappush(Q, (-(A[nex[0]] + B[nex[1]] + C[nex[2]]),) + nex)
    nex = (now[1], now[2] + 1, now[3])
    if not nex in V and isIn(nex):
        V.add(nex)
        heapq.heappush(Q, (-(A[nex[0]] + B[nex[1]] + C[nex[2]]),) + nex)
    nex = (now[1], now[2], now[3] + 1)
    if not nex in V and isIn(nex):
        V.add(nex)
        heapq.heappush(Q, (-(A[nex[0]] + B[nex[1]] + C[nex[2]]),) + nex)
