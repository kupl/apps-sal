from collections import defaultdict
import heapq

INF_MAX = 10 ** 10


def set_remove(hp, dct, x):
    dct[x] += 1


def set_getmin(hp, dct):
    while True:
        if len(hp) == 0:
            return INF_MAX
        a = hp[0]
        if dct[a]:
            dct[a] -= 1
            heapq.heappop(hp)
        else:
            return a


N, Q = map(int, input().split())
A = [0] * N
B = [0] * N
C = [0] * Q
D = [0] * Q
E = [-1] * N
G = set()
hps = dict()
dcts = dict()
b, c, d, FROM, TO = 0, 0, 0, 0, 0
for i in range(N):
    A[i], b = map(int, input().split())
    b -= 1
    B[i] = b
    G.add(b)
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    C[i] = c
    D[i] = d
    G.add(d)

G.add(-1)
for g in G:
    hps[g] = list()
    dcts[g] = defaultdict(int)

for i in range(N):
    b = B[i]
    heapq.heappush(hps[b], -A[i])
    E[i] = b

hps[-1] = [-hps[b][0] for b in set(B)]
heapq.heapify(hps[-1])

for i in range(Q):
    c = C[i]
    FROM = E[c]
    TO = D[i]
    E[c] = TO
    c = A[c]
    # 転校元での処理
    b = set_getmin(hps[FROM], dcts[FROM])
    b *= -1
    if c == b:
        set_remove(hps[-1], dcts[-1], c)
        set_remove(hps[FROM], dcts[FROM], -c)
        d = set_getmin(hps[FROM], dcts[FROM])
        if d != INF_MAX:
            d *= -1
            heapq.heappush(hps[-1], d)
    else:
        set_remove(hps[FROM], dcts[FROM], -c)

    # 転校先での処理
    b = set_getmin(hps[TO], dcts[TO])
    if b != INF_MAX:
        b *= -1
        if c > b:
            set_remove(hps[-1], dcts[-1], b)
            heapq.heappush(hps[-1], c)
    else:
        heapq.heappush(hps[-1], c)
    heapq.heappush(hps[TO], -c)
    print(set_getmin(hps[-1], dcts[-1]))
