import queue
n, m = list(map(int, input().split()))
route = [[] for _ in range(n)]
vals = []
for _ in range(m):
    a, b = list(map(int, input().split()))
    route[a-1].append(b-1)
    route[b-1].append(a-1)
    vals.append([a-1, b-1])
ans = m
for i in range(m):
    route2 = set()
    q = queue.Queue()
    q.put(0)
    route[vals[i][0]].remove(vals[i][1])
    route[vals[i][1]].remove(vals[i][0])
    while not q.empty():
        a = q.get()
        if not a in route2:
            route2.add(a)
            for j in route[a]:
                q.put(j)
        if len(route2) == n:
            ans -= 1
            break
    route[vals[i][0]].append(vals[i][1])
    route[vals[i][1]].append(vals[i][0])
print(ans)
        

