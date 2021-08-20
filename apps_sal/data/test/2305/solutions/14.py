import sys
import itertools
sys.setrecursionlimit(3 * 10 ** 5)


class Node:

    def __init__(self, color):
        self.color = int(color) - 1
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    @staticmethod
    def prepare_nodes(n):
        nodes = tuple(map(Node, input().split()))
        for _ in range(n - 1):
            (a, b) = [int(x) - 1 for x in input().split()]
            nodes[a].add_child(nodes[b])
            nodes[b].add_child(nodes[a])
        return nodes


def main():
    n = int(input())
    nodes = Node.prepare_nodes(n)
    dp = [0 for _ in range(n)]
    ans_list = [n * (n + 1) // 2 for _ in range(n)]

    def update_ans(s, color):
        ans_list[color] -= (s + dp[color]) * (s + dp[color] + 1) // 2

    def dfs(s, node, parent):
        color = node.color
        pre_s = s + dp[color]
        for child in node.children:
            if child == parent:
                continue
            dp[color] = -s
            s = dfs(s, child, node)
            update_ans(s, color)
        s += 1
        dp[color] = pre_s - s
        return s
    s = dfs(0, nodes[0], Node(-1))
    for i in range(n):
        update_ans(s, i)
        print(ans_list[i])


main()
