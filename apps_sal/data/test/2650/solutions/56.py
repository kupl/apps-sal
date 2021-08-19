import heapq
(N, Q) = map(int, input().split())
ST = [0] * (N + 1)
kid_Add = [[] for _ in range(2 * 10 ** 5 + 1)]
kid_Del = [[] for _ in range(2 * 10 ** 5 + 1)]
max_Add = []
max_Del = []
heapq.heapify(kid_Add)
heapq.heapify(kid_Del)
heapq.heapify(max_Add)
heapq.heapify(max_Del)
for i in range(N):
    (A, B) = map(int, input().split())
    heapq.heappush(kid_Add[B], -1 * A)
    ST[i + 1] = (A, B)
for i in range(2 * 10 ** 5 + 1):
    if kid_Add[i]:
        heapq.heappush(max_Add, -1 * kid_Add[i][0])


def deleteHeap(x, y):
    while y and x[0] == y[0]:
        heapq.heappop(x)
        heapq.heappop(y)


for j in range(Q):
    (C, D) = map(int, input().split())
    (s, t) = ST[C]
    if not kid_Add[D]:
        Ne_S = 0
    else:
        Ne_S = kid_Add[D][0]
    Ol_S = kid_Add[t][0]
    heapq.heappush(kid_Add[D], -1 * s)
    heapq.heappush(kid_Del[t], -1 * s)
    deleteHeap(kid_Add[t], kid_Del[t])
    if Ne_S > -1 * s:
        heapq.heappush(max_Add, s)
        if Ne_S != 0:
            heapq.heappush(max_Del, -1 * Ne_S)
    if Ol_S == -1 * s:
        heapq.heappush(max_Del, s)
        if kid_Add[t]:
            heapq.heappush(max_Add, -1 * kid_Add[t][0])
    deleteHeap(max_Add, max_Del)
    print(max_Add[0])
    ST[C] = (s, D)
