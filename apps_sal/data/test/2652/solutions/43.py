def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    xy = []
    node = [[]for _ in range(n)]
    for i in range(n):
        x, y = map(int, input().split())
        xy.append((i, x, y))
    xy.sort(key=lambda x: x[1])
    for i in range(len(xy) - 1):
        node[xy[i][0]].append((abs(xy[i][1] - xy[i + 1][1]), xy[i + 1][0]))  # dis,num
        node[xy[i + 1][0]].append((abs(xy[i][1] - xy[i + 1][1]), xy[i][0]))  # dis,num
    xy.sort(key=lambda x: x[2])
    for i in range(len(xy) - 1):
        node[xy[i][0]].append((abs(xy[i][2] - xy[i + 1][2]), xy[i + 1][0]))  # dis,num
        node[xy[i + 1][0]].append((abs(xy[i][2] - xy[i + 1][2]), xy[i][0]))  # dis,num
    from heapq import heappop, heappush
    visited = [False] * n
    visited[0] = True
    pq = []
    for x in node[0]:
        heappush(pq, (x[0], x[1]))
    ans = 0
    for _ in range(n - 1):
        while True:
            u = heappop(pq)
            if visited[u[1]] == False:
                break
        ans += u[0]
        pre_dis = u[0]
        u_dis = u[0]
        u_num = u[1]
        ans += abs(u_dis - pre_dis)
        visited[u_num] = True
        for x in node[u_num]:
            x_dis = x[0]
            x_num = x[1]
            if visited[x_num] == False:
                heappush(pq, (x_dis, x_num))
    print(ans)


def __starting_point():
    main()


__starting_point()
