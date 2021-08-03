import sys
import threading
sys.setrecursionlimit(10**6)
threading.stack_size(10**8)


def main():
    n = int(input().strip())
    son_tree = dict()
    min_max = [0] + [int(i) for i in input().strip().split()]
    for child, parent in enumerate(map(int, input().strip().split()), 2):
        if parent not in son_tree:
            son_tree[parent] = [child]
        else:
            son_tree[parent].append(child)
    leaf_ctr = 0
    dp = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        if i not in son_tree:
            leaf_ctr += 1
            dp[i] = 1

    visited = set()

    def dfs(node):
        if node not in visited:
            visited.add(node)
            if node not in son_tree:
                return 1
            if min_max[node]:
                for i in son_tree[node]:
                    dfs(i)
                dp[node] = min(dp[k] for k in son_tree[node])
                return 0
            else:
                for i in son_tree[node]:
                    dfs(i)
                dp[node] = sum(dp[k] for k in son_tree[node])
                return 0
    dfs(1)
    print(leaf_ctr - dp[1] + 1)


def __starting_point():
    t = threading.Thread(target=main)
    t.start()
    t.join()


__starting_point()
