import math
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    min_max = list(map(int, input().split()))
    tree_input = list(map(int, input().split()))
    tree = [[] for _ in range(n)]
    for v in range(n - 1):
        parent = tree_input[v] - 1
        tree[parent].append(v + 1)
    leaves = [0 for _ in range(n)]
    stack = [0]
    pos = 0
    while pos < len(stack):
        for child in tree[stack[pos]]:
            stack.append(child)
        pos += 1
    for pos in range(len(stack) - 1, -1, -1):
        node = stack[pos]
        if len(tree[node]) == 0:
            leaves[node] = 1
        else:
            for child in tree[node]:
                leaves[node] += leaves[child]
    node_max = [0] * n
    for pos in range(len(stack) - 1, -1, -1):
        node = stack[pos]
        if len(tree[node]) == 0:
            node_max[node] = 1
        elif min_max[node] == 1:
            best = math.inf
            for child in tree[node]:
                if leaves[child] - node_max[child] < best:
                    best = leaves[child] - node_max[child]
            node_max[node] = leaves[node] - best
        else:
            optimal = 1
            for child in tree[node]:
                optimal += node_max[child] - 1
            node_max[node] = optimal
    print(node_max[0])


def __starting_point():
    main()


__starting_point()
