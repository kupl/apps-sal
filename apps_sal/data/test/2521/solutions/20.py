import heapq
n = int(input())
A = list(map(int, input().split()))
Q0 = []
Q1 = []
Ana = [0] * (3 * n)
M = [[A[n + i], n + i] for i in range(2 * n)]
M.sort()
msum = sum([M[i][0] for i in range(n)])
ans = sum(A[:n]) - msum
ans0 = ans
for i in range(n):
    heapq.heappush(Q0, A[i])
    heapq.heappush(Q1, [M[n + i][0], M[n + i][1]])
    Ana[M[n + i][1]] = 1
for i in range(n):
    if Ana[n + i] == 0:
        heapq.heappush(Q0, A[n + i])
        ans0 += A[n + i] * 2
        ochi = heapq.heappop(Q0)
        ans0 -= ochi
        agari = heapq.heappop(Q1)
        while Ana[agari[1]] == 0:
            agari = heapq.heappop(Q1)
        Ana[agari[1]] = 0
        ans0 -= agari[0]
    else:
        Ana[n + i] = 0
        heapq.heappush(Q0, A[n + i])
        ans0 += A[n + i]
        ochi = heapq.heappop(Q0)
        ans0 -= ochi
    ans = max(ans, ans0)
saigo = sum(sorted(A[:n * 2])[n:]) - sum(A[n * 2:])
ans = max(ans, saigo)
print(ans)
