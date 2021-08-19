class Node:

    def __init__(self):
        self.adj = []


def solve():
    (n, x) = list(map(int, input().split()))
    x -= 1
    nodes = [Node() for _ in range(n)]
    for _ in range(n - 1):
        (u, v) = list(map(int, input().split()))
        u -= 1
        v -= 1
        nodes[u].adj.append(v)
        nodes[v].adj.append(u)
    if len(nodes[x].adj) == 1 or n == 1:
        return 'Ayush'
    return 'Ashish' if n % 2 == 1 else 'Ayush'


t = int(input())
for _ in range(t):
    print(solve())
