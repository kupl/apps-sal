import heapq


N = int(input())

P = list(map(int, input().split()))


Llis = []
Rlis = []

for i in range(N):

    Llis.append([N, N])
    Rlis.append([N, N])
    P[i] -= 1


LQ1 = []
LQ2 = []

for i in range(N):

    while len(LQ2) > 0 and LQ2[0][0] < P[i]:
        Llis[LQ2[0][1]][1] = i
        heapq.heappop(LQ2)

    while len(LQ1) > 0 and LQ1[0][0] < P[i]:
        Llis[LQ1[0][1]][0] = i
        heapq.heappush(LQ2, LQ1[0])
        heapq.heappop(LQ1)

    heapq.heappush(LQ1, [P[i], i])

P.reverse()
LQ1 = []
LQ2 = []

for i in range(N):

    while len(LQ2) > 0 and LQ2[0][0] < P[i]:
        Rlis[LQ2[0][1]][1] = i
        heapq.heappop(LQ2)

    while len(LQ1) > 0 and LQ1[0][0] < P[i]:
        Rlis[LQ1[0][1]][0] = i
        heapq.heappush(LQ2, LQ1[0])
        heapq.heappop(LQ1)

    heapq.heappush(LQ1, [P[i], i])


Rlis.reverse()
#print (Llis,Rlis)

ans = 0
P.reverse()

for i in range(N):

    Llenge = Llis[i][1] - Llis[i][0]
    Rlenge = 1 + max(0, i - (N - Rlis[i][0]))

    ans += (P[i] + 1) * Llenge * Rlenge
    #print (P[i] , Llenge , Rlenge)

P.reverse()
Rlis.reverse()
Llis.reverse()

for i in range(N):

    Rlenge = Rlis[i][1] - Rlis[i][0]
    Llenge = 1 + max(0, i - (N - Llis[i][0]))

    ans += (P[i] + 1) * Llenge * Rlenge
    #print (P[i],Llenge,Rlenge)

print(ans)
