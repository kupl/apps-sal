import heapq
N, C = map(int, input().split())

stc = [list(map(int, input().split())) for _ in range(N)]

stc.sort()

lst = []
hq = [[-1, -1]]
heapq.heapify(hq)
ans = 1
for i in range(N):
    p = stc[i]
    q = heapq.heappop(hq)
    if p[0] < q[0]:
        heapq.heappush(hq, q)

        ans += 1

    elif p[0] == q[0]:
        lst = []
        jdg2 = True

        while p[0] == q[0] and p[2] >= q[1]:
            if p[2] == q[1]:

                jdg2 = False
            else:
                lst.append(q)
            if hq:
                q = heapq.heappop(hq)
            else:
                break
        if jdg2:
            ans += 1
        if p[0] != q[0] or p[2] < q[1]:
            heapq.heappush(hq, q)

        for k in lst:
            heapq.heappush(hq, k)

    heapq.heappush(hq, [p[1], p[2]])

print(ans)
