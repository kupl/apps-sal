class Node:
    def __init__(self, i):
        self.i = i
        self.adj = []

def draw_hedgehog(n, nodes):
    tail_length = [1] * n
    best_beauty = len(nodes[0].adj)

    for i in range(1, n):
        max_so_far = tail_length[i]
        best_length = tail_length[i]
        spines = len(nodes[i].adj)
        for j in nodes[i].adj:
            if j < i:
                beauty = (tail_length[j] + 1) * spines
                if beauty > max_so_far:
                    max_so_far = beauty
                    best_length = tail_length[j] + 1
        tail_length[i] = best_length
        if max_so_far > best_beauty:
            best_beauty = max_so_far

    return best_beauty

def __starting_point():
    n, m = input().split()
    n, m = int(n), int(m)
    nodes = [Node(i) for i in range(n)]
    for k in range(m):
        u, v = input().split()
        u, v = int(u) - 1, int(v) - 1
        nodes[u].adj.append(v)
        nodes[v].adj.append(u)

    result = draw_hedgehog(n, nodes)
    print(result)

__starting_point()
