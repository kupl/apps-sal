n = int(input())
A = list(map(int, input().split()))
A = [a-1 for a in A]

P = [-1]*n
for i, a in enumerate(A):
    P[a] = i

#print(P)

R = [[n]*2 for _ in range(n)]
q = []
import heapq
heapq.heapify(q)
for i in range(n):
    temp = []
    while q:
        if q[0][0] < A[i]:
            v, j = heapq.heappop(q)
            R[v][j] = i
            if j == 0:
                temp.append((v, j+1))
        else:
            break
    heapq.heappush(q, (A[i], 0))
    for v, j in temp:
        heapq.heappush(q, (v, j))

#print(R)

L = [[-1]*2 for _ in range(n)]
q = []
import heapq
heapq.heapify(q)
for i in reversed(list(range(n))):
    temp = []
    while q:
        if q[0][0] < A[i]:
            v, j = heapq.heappop(q)
            L[v][j] = i
            if j == 0:
                temp.append((v, j+1))
        else:
            break
    heapq.heappush(q, (A[i], 0))
    for v, j in temp:
        heapq.heappush(q, (v, j))

#print(L)
ans = 0
for i in range(n-1):
    p = P[i]
    l1 = L[i][0]
    l2 = L[i][1]
    r1 = R[i][0]
    r2 = R[i][1]
    ans += ((l1-l2)*(r1-p)+(r2-r1)*(p-l1))*(i+1)
print(ans)

