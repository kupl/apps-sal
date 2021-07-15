from queue import Queue


def BFS(v):
    st = Queue()
    st.put(v)

    while not st.empty():
        u = st.get()

        count = 0
        for v in graph[u]:
            if graph[v] == list():
                count += 1

            else:
                st.put(v)

        if count < 3:
            return False

    return True


n = int(input())

graph = {i: list() for i in range(1, n + 1)}
for i in range(2, n + 1):
    j = int(input())

    graph[j].append(i)

print(('No', 'Yes')[BFS(1)])

