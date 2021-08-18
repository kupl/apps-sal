
import heapq
M = 2 * (10**5)
N, Q = list(map(int, input().split()))
enji = []
for i in range(N):
    enji.append(tuple(map(int, input().split())))

belong = [0] * N
K = [[] for _ in range(M)]
for i, (a, b) in enumerate(enji):
    heapq.heappush(K[b - 1], (-a, i))
    belong[i] = b - 1


E = []
for i in range(M):
    if K[i] != []:
        heapq.heappush(E, (K[i][0][0] * -1, K[i][0][1], belong[K[i][0][1]]))


def insert_enji(x, y):
    if K[y] == [] or K[y][0][0] > enji[x][0] * -1:
        heapq.heappush(K[y], (enji[x][0] * -1, x))
        heapq.heappush(E, (K[y][0][0] * -1, K[y][0][1], belong[K[y][0][1]]))
    else:
        heapq.heappush(K[y], (enji[x][0] * -1, x))


def mainte_K(x, y):
    flg = False
    while K[y]:
        if belong[K[y][0][1]] == y:
            break
        else:
            heapq.heappop(K[y])
            flg = True
    if flg == True and K[y] != []:
        heapq.heappush(E, (-K[y][0][0], K[y][0][1], y))


def mainte_E():
    while E:
        if K[E[0][2]] != [] and K[E[0][2]][0] == (E[0][0] * -1, E[0][1]):
            break
        else:
            heapq.heappop(E)


for i in range(Q):
    c, d = list(map(int, input().split()))
    c -= 1
    d -= 1
    old = belong[c]
    belong[c] = d
    insert_enji(c, d)
    mainte_K(c, old)
    mainte_E()
    print((E[0][0]))
