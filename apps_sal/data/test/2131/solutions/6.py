n = int(input())
graph = [[] for i in range(n + 1)]
center = None
should_continue = True
ends = set()
for i in range(n - 1):
    parameters = [int(s) for s in input().split(" ")]
    from_ = parameters[0]
    to = parameters[1]
    # print(graph)
    # print(from_)
    # if not graph[from_]:
    #     graph[from_] = []
    # if not graph[to]:
    #     graph[to] = []
    graph[from_].append(to)
    graph[to].append(from_)
    if len(graph[from_]) > 2:
        if center and center != from_:
            should_continue = False
            break
        center = from_

    if len(graph[to]) > 2:
        if center and center != to:
            should_continue = False
            break
        center = to

    if len(graph[from_]) == 1:
        ends.add(from_)
    else:
        ends.discard(from_)

    if len(graph[to]) == 1:
        ends.add(to)
    else:
        ends.discard(to)

if not should_continue:
    print("No")
else:
    print("Yes")

    if center == None:
        print("1")
        print(str(ends.pop()) + " " + str(ends.pop()))
    else:
        print(len(graph[center]))
        for i in ends:
            print(str(center) + " " + str(i))
