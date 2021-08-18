
import sys


def explore(src, prob, length, adj_mat, gains, visited):
    nexts = set(adj_mat[src]) - visited
    if nexts:
        go_prob = 1 / len(nexts)
        length += 1
        for dst in nexts:
            visited.add(dst)
            explore(dst, prob * go_prob, length, adj_mat, gains, visited)
    else:
        gains[src] += prob * length


def main():
    n = int(sys.stdin.readline())
    adj_mat = [[] for __ in range(n)]
    node_exp = [0 for __ in range(n)]
    for __ in range(n - 1):
        u, v = list(map(int, sys.stdin.readline().split()))
        adj_mat[u - 1].append(v - 1)
        adj_mat[v - 1].append(u - 1)
    stk = [0]
    visited = set([0])
    prob = [1] * n
    length = [0] * n
    while stk:
        nxt = stk.pop()
        nexts = set(adj_mat[nxt]) - visited
        if nexts:
            go_prob = 1 / len(nexts)
            for dst in nexts:
                visited.add(dst)
                stk.append(dst)
                prob[dst] *= prob[nxt] * go_prob
                length[dst] = length[nxt] + 1
        else:
            node_exp[nxt] += prob[nxt] * length[nxt]

    print("{:.13f}".format(sum(node_exp)))


main()
