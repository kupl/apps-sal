from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline

DEBUG = False
INF = float('inf')
MAX_N = 50
MAX_A = 50

N, M, S = list(map(int, input().split()))
U = []
V = []
A = []
B = []
C = []
D = []

connect = [[] for _ in range(N)]
for _ in range(M):
    u, v, a, b = list(map(int, input().split()))
    U.append(u)
    V.append(v)
    A.append(a)
    B.append(b)
    connect[u - 1].append([v - 1, a, b])
    connect[v - 1].append([u - 1, a, b])
for _ in range(N):
    c, d = list(map(int, input().split()))
    C.append(c)
    D.append(d)

if DEBUG:
    print(("U: {}".format(U)))
    print(("V: {}".format(V)))
    print(("A: {}".format(A)))
    print(("B: {}".format(B)))
    print(("C: {}".format(C)))
    print(("D: {}".format(D)))
    print(("connect: {}".format(connect)))

MAX_N = N
MAX_A = max(A)
MAX_MONEY = MAX_N * MAX_A
S = min(S, MAX_MONEY - 1)

node = [INF for _ in range(MAX_MONEY * N)]
hq = []
heappush(hq, (0, S))
while hq:
    time, current_node = heappop(hq)
    if DEBUG:
        print(("time: {}, current_node: {}, len(hq): {}".format(time, current_node, len(hq))))
    if time < node[current_node]:
        node[current_node] = time
    else:
        continue
    index_city = current_node // MAX_MONEY
    money = current_node % MAX_MONEY
    if DEBUG:
        print(("money: {}".format(money)))

    for index_next_city, a, b in connect[index_city]:
        if money >= a and time + b < node[index_next_city * MAX_MONEY + money - a]:
            heappush(hq, (time + b, index_next_city * MAX_MONEY + money - a))
    if money < MAX_MONEY - 1:
        heappush(hq, (time + D[index_city], min(money + C[index_city], MAX_MONEY - 1) + MAX_MONEY * index_city))

for i in range(1, N):
    if DEBUG:
        print(("node{}: {}".format(i, node[MAX_MONEY * i:MAX_MONEY * (i + 1)])))
    print((min(node[MAX_MONEY * i:MAX_MONEY * (i + 1)])))
