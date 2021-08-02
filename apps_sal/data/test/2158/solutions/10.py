import sys
mod = 1000000007
def get_array(): return list(map(int, sys.stdin.readline().split()))
def get_ints(): return map(int, sys.stdin.readline().split())
def input(): return sys.stdin.readline()
def print_array(a): print(" ".join(map(str, a)))


def maxCost(cost, tree, c, p):
    frnds = tree[c]
    if len(frnds) == 1 and frnds[0] == p: return 0
    l = []
    for frnd in frnds:
        if frnd != p: l.append(cost[c][frnd] + maxCost(cost, tree, frnd, c))
    return max(l)


def main():
    n = int(input())
    cost = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v, c = get_ints()
        tree[u].append(v)
        tree[v].append(u)
        cost[u][v] = cost[v][u] = c
    print(maxCost(cost, tree, 0, 0))


def __starting_point():
    main()


__starting_point()
