def f():
    n = int(input())
    if n == 1:
        print(0)
        return
    road = {}
    visited = {}
    for i in range(n - 1):
        (u, v) = input().split()
        if u in road:
            road[u].append(v)
        else:
            road[u] = [v]
        if v in road:
            road[v].append(u)
        else:
            road[v] = [u]
        visited[u] = False
        visited[v] = False
    prob = {}
    length = {}
    res = []
    queue = []
    for k in road['1']:
        prob[k] = 1.0 / len(road['1'])
        length[k] = 1
        queue.append(k)
        visited['1'] = True
    while len(queue) > 0:
        cur = queue[0]
        del queue[0]
        dest = []
        for k in road[cur]:
            if not visited[k]:
                dest.append(k)
        if len(dest) == 0:
            res.append((cur, prob[cur], length[cur]))
            continue
        for k in dest:
            prob[k] = prob[cur] / len(dest)
            length[k] = length[cur] + 1
            queue.append(k)
            visited[cur] = True
    val = 0.0
    for item in res:
        val += item[1] * item[2]
    print(val)


f()
