import collections

n = list(map(int, input().split()))[0]
di = ((2, 2), (-2, 2), (-2, -2), (2, -2))


def bfs(graph, x, y, tx, ty):
    vis = set()
    queue = collections.deque()
    queue.append((x, y))
    vis.add((x, y))
    dis = {}
    dis[(x, y)] = 0

    while queue:
        elem = queue.popleft()
        #print (elem)

        for direction in di:
            new_elem = (elem[0] + direction[0], elem[1] + direction[1])
            #print (new_elem)
            if new_elem[0] >= 0 and new_elem[1] >= 0 and new_elem[0] < 8 and new_elem[1] < 8:
                if new_elem not in vis:
                    vis.add(new_elem)
                    queue.append(new_elem)
                    dis[new_elem] = dis[elem] + 1
#                    print (elem,  new_elem, dis[new_elem])

    if (tx, ty) not in vis:
        return (False, 0)
    return (True, dis[(tx, ty)])


for cc in range(n):
    datamap = []

    for i in range(8):
        datamap.append(input())

    ans = []
    for i in range(len(datamap)):
        for j in range(len(datamap[i])):
            if datamap[i][j] == 'K':
                ans.append(i)
                ans.append(j)

    ans = bfs(datamap, ans[0], ans[1], ans[2], ans[3])
    #print (ans)
    if ans[0] and ans[1] % 2 == 0:
        print("YES")
    else:
        print("NO")

    if cc != n - 1:
        input()
