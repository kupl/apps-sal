import sys
from heapq import heapify, heappop, heappushpop, heappush

M = 2*10**5
input = sys.stdin.readline
N, Q = list(map(int, input().split()))
rates = [0] * N
wheres = [0] * N
kgs = [[(0, 0)] for _ in range(M)]
for i in range(N):
    a, b = list(map(int, input().split()))
    rates[i] = a
    wheres[i] = b-1
    heappush(kgs[b-1], (-a, i))
rankers = []
for kg in kgs:
    v = kg[0]
    if v[0] != 0:
        heappush(rankers, (-v[0], v[1], wheres[v[1]]))

def fetch_max(i):
    while True:
        v = kgs[i][0]
        if v[0] == 0 or wheres[v[1]] == i:
            return v
        heappop(kgs[i])

def fetch_min():
    while True:
        v = rankers[0]
        w = fetch_max(v[2])
        if w[0] != 0 and w[1] == v[1]:
            return v
        heappop(rankers)

def solve():
    for _ in range(Q):
        c, d = list(map(int, input().split()))
        ibkg, iakg = wheres[c-1], d-1
        wheres[c-1] = d-1
        heappush(kgs[iakg], (-rates[c-1], c-1))

        bef = fetch_max(ibkg)
        heappush(rankers, (-bef[0], bef[1], ibkg))

        aft = kgs[iakg][0]
        heappush(rankers, (-aft[0], aft[1], iakg))

        print((fetch_min()[0]))

def __starting_point():
    solve()

__starting_point()
