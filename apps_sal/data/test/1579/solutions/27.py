import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
edges = [[] for i in range(2 * 10 ** 5)]
for i in range(n):
    (xi, yi) = map(int, input().split())
    xi -= 1
    yi = yi - 1 + 10 ** 5
    edges[xi].append(yi)
    edges[yi].append(xi)
already = set([])


def dfs(x, y, node):
    if node in already:
        return (x, y)
    if node < 10 ** 5:
        x += 1
    else:
        y += 1
    already.add(node)
    for next_node in edges[node]:
        (x, y) = dfs(x, y, next_node)
    return (x, y)


num = 0
for i in range(10 ** 5):
    (x, y) = dfs(0, 0, i)
    num += x * y
print(num - n)
