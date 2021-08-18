
class node():
    def __init__(self, v, edges):
        self.value = v
        self.edges = edges


n = int(input())
a = [int(i) for i in input().split(" ")]


def fun(a):
    nodes = {}
    for i in range(60):
        k = 0
        value = 1 << i
        i_edges = set()
        for j in a:
            if value & j > 0:
                k += 1
                if k > 2:
                    del i_edges
                    del nodes
                    return 3
                i_edges.add(j)
        for j in i_edges:
            if j not in nodes:
                if (i_edges.difference({j})) != 0:
                    nodes[j] = node(j, i_edges.difference({j}))
            else:
                nodes[j].edges = nodes[j].edges.union(i_edges.difference({j}))
    return nodes


def find_short_path(v1, v2):
    length = 0
    v2 = {v2}
    setic = set()
    set_was = set()
    while (v1 not in setic):
        del setic
        setic = set()
        for i in v2:
            setic = setic.union(nodes[i].edges.difference(set_was))
        set_was = set_was.union(setic)
        if len(setic) == 0:
            del v2
            return 0
        length += 1
        del v2
        v2 = setic.copy()
    del set_was
    del setic
    return length


nodes = fun(a)
if type(nodes) == int:
    print(3)
else:
    mass = []
    while len(nodes.keys()) != 0:
        i = list(nodes.keys())[0]
        if len(nodes[i].edges) != 0:

            first_v = i
            second_v = nodes[first_v].edges.pop()
            nodes[second_v].edges.remove(first_v)
            length = 0
            if len(nodes[first_v].edges) == 0:
                nodes.pop(first_v)
            elif len(nodes[second_v].edges) == 0:
                nodes.pop(second_v)
            else:
                length = find_short_path(first_v, second_v)

            if length:
                mass.append(length + 1)
        else:
            nodes.pop(i)

    if len(mass) != 0:
        print(min(mass))
    else:
        print(-1)
