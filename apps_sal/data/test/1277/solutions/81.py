from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)


def depth(adj, node, parent=None):
    ret = 0
    for child in adj[node]:
        if child == parent:
            continue
        d = depth(adj, child, node) + 1
        ret = max(ret, d)
    return ret


def main():
    (N, U, V) = list(map(int, input().split(' ')))
    U -= 1
    V -= 1
    adj = defaultdict(list)
    for _ in range(N - 1):
        (A, B) = list(map(lambda x: int(x) - 1, input().split(' ')))
        adj[A].append(B)
        adj[B].append(A)
    path = [-1] * N

    def find_path_on_tree(to_node, node, parent=None, d=0):
        if node == to_node:
            path[d] = node
            return True
        for child in adj[node]:
            if child == parent:
                continue
            if not find_path_on_tree(to_node, child, node, d + 1):
                continue
            path[d] = node
            return True
        return False
    find_path_on_tree(U, V)
    path = [node for node in path if node != -1]
    dist = len(path) - 1
    partial_depth = depth(adj, path[dist // 2 + 1], path[dist // 2])
    print(partial_depth + dist // 2)


def __starting_point():
    main()


__starting_point()
