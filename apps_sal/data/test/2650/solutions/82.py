import heapq
N, Q = list(map(int, input().split()))
A = [0 for i in range(N)]
B = [0 for i in range(N)]
C = [0 for i in range(Q)]
D = [0 for i in range(Q)]
for i in range(N):
    A[i], B[i] = list(map(int, input().split()))
    B[i] -= 1
for i in range(Q):
    C[i], D[i] = list(map(int, input().split()))
    C[i] -= 1
    D[i] -= 1
nowbelongs = [B[i] for i in range(N)]
maxrate = []
kindergarden = [[] for i in range(2 * 10**5)]
for i in range(N):
    heapq.heappush(kindergarden[B[i]], (-A[i], i))


def saikyo_enji(k):
    while(kindergarden[k]):
        minusrate, index = kindergarden[k][0]
        if nowbelongs[index] == k:
            return index
        else:
            heapq.heappop(kindergarden[k])
    return -1


for k in range(2 * 10**5):
    i = saikyo_enji(k)
    if i != -1:
        heapq.heappush(maxrate, (A[i], i))
for j in range(Q):
    i = C[j]
    oldbelongs = nowbelongs[i]
    nowbelongs[i] = -1
    if saikyo_enji(oldbelongs) != -1:
        heapq.heappush(maxrate, (A[saikyo_enji(oldbelongs)], saikyo_enji(oldbelongs)))
    heapq.heappush(kindergarden[D[j]], (-A[C[j]], C[j]))
    nowbelongs[C[j]] = D[j]
    heapq.heappush(maxrate, (A[saikyo_enji(D[j])], saikyo_enji(D[j])))
    while(maxrate):
        rate, index = maxrate[0]
        if saikyo_enji(nowbelongs[index]) == index:
            print(rate)
            break
        else:
            heapq.heappop(maxrate)
