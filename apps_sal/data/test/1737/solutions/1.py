from queue import Queue


def BFS(v):
    nonlocal ans

    stack = Queue()
    stack.put(v)

    used = {p[0]: False for p in list(graph.keys())}
    used[v[0]] = True

    while True:
        set_ = dict()
        st = Queue()

        while not stack.empty():
            v = stack.get()

            for u in graph[v]:
                n_ = u[0]
                if not used[n_]:
                    try:
                        set_[n_] = max(set_[n_], u[1])
                    except KeyError:
                        set_[n_] = u[1]

        for el in list(set_.items()):
            ans.append(el)
            st.put(el)
            used[el[0]] = True

        if st.empty():
            break

        while not st.empty():
            stack.put(st.get())


n = int(input())
graph = dict()

for i in range(n):
    name, ver = input().split()
    k = int(input())
    temp = set()

    for j in range(k):
        name_, ver_ = input().split()
        temp.add((name_, int(ver_)))

    tup = (name, int(ver))
    graph[tup] = temp

    if i == 0:
        PP = tup

    if i + 1 != n:
        input()

ans = list()

BFS(PP)

print(len(ans))
print('\n'.join([' '.join(map(str, el)) for el in sorted(ans, key=lambda x: x[0])]))

