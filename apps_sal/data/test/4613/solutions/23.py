import copy


def main():
    N, M = [int(n) for n in input().split(" ")]
    edges = [[] for i in range(N)]
    # edges[i] : edges from vertex i
    r = []
    for i in range(M):
        a, b = [int(x) for x in input().split(" ")]
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
        r.append([a - 1, b - 1])
    cnt = 0
    for i in range(len(r)):
        if not isConnected(edges, r[i]):
            cnt += 1
    print(cnt)


def isConnected(edges, remove_edge):
    n_v = len(edges)
    checked = [0] * n_v
    to_check = [0]
    e = copy.deepcopy(edges)
    e[remove_edge[0]].remove(remove_edge[1])
    e[remove_edge[1]].remove(remove_edge[0])
    while len(to_check) > 0:
        checking = to_check.pop(0)
        checked[checking] = 1
        for i in e[checking]:
            if checked[i] == 1:
                continue
            else:
                to_check.append(i)
    if n_v == sum(checked):
        return True
    else:
        return False


main()
