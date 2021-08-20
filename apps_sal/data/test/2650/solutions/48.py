def solve():
    import heapq
    M = 2 * 10 ** 5
    (N, Q) = list(map(int, input().split()))
    (As, Bs) = ([], [])
    yochien = [list() for _ in range(M)]
    for i in range(N):
        (a, b) = list(map(int, input().split()))
        b = b - 1
        (As.append(a), Bs.append(b))
        heapq.heappush(yochien[b], (-a, i))
    top = []
    for m in range(M):
        if yochien[m]:
            heapq.heappush(top, (-yochien[m][0][0], yochien[m][0][1], m))
    for _ in range(Q):
        (c, d) = list(map(int, input().split()))
        (c, d) = (c - 1, d - 1)
        before = Bs[c]
        Bs[c] = d
        heapq.heappush(yochien[d], (-As[c], c))
        if yochien[d][0][1] == c:
            heapq.heappush(top, (As[c], c, d))
        flag = False
        while yochien[before] and Bs[yochien[before][0][1]] != before:
            heapq.heappop(yochien[before])
            flag = True
        if flag and yochien[before]:
            heapq.heappush(top, (-yochien[before][0][0], yochien[before][0][1], before))
        while not yochien[top[0][2]] or yochien[top[0][2]][0][1] != top[0][1]:
            heapq.heappop(top)
        print(top[0][0])


def __starting_point():
    solve()


__starting_point()
