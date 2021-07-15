n, k = list(map(int, input().split()))
d = list(map(int, input().split()))
max_d = max(d)
levels = [[] for i in range(max_d+1)]
graph = {}
for i in range(len(d)):
    levels[d[i]].append(i+1)

def do_this():
    nonlocal n,k, d, max_d, levels, graph
    q = []
    last_level = levels[0]
    if len(last_level) != 1:
        print(-1)
        return
    for i in range(1, max_d+1):
        if i == 2:
            k = k-1
        if k == 0:
            print(-1)
            return
        cur_level = levels[i]
        for j in range(len(cur_level)):
            if j/k >= len(last_level):
                print(-1)
                return
            q.append((last_level[int(j/k)], cur_level[j]))
        last_level = cur_level
    print(len(q))
    for a,b in q: print(a, b)

do_this()

