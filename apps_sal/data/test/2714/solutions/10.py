from collections import defaultdict
import sys
input = sys.stdin.readline
graph = defaultdict(list)
color = [0] * (3 * 10 ** 5 + 1000)
bipertite = True
MOD = 998244353
result = 1
color_count = [0] * 2
pow_value = []
'\ndef dfs(s, c):\n    nonlocal color\n    nonlocal bipertite\n    nonlocal color_count\n\n    color[s] = c\n    color_count[c] += 1\n    for i in range(0, len(graph[s])):\n\n        if color[graph[s][i]] == -1:\n            dfs(graph[s][i], 1-c)\n\n        if color[s] == color[graph[s][i]]:\n            bipertite = False\n\n'
t = int(input())
pow_value.append(1)
for i in range(1, 3 * 10 ** 5 + 1000):
    next_value = pow_value[i - 1] * 2 % MOD
    pow_value.append(next_value)
while t:
    (n, m) = list(map(int, input().split()))
    if m == 0:
        print(pow(3, n, MOD))
        t -= 1
        continue
    graph.clear()
    bipertite = True
    result = 1
    for node in range(0, n + 1):
        color[node] = -1
    while m:
        (u, v) = list(map(int, input().split()))
        graph[u].append(v)
        graph[v].append(u)
        m -= 1
    for i in range(1, n + 1):
        if color[i] != -1:
            continue
        bipertite = True
        color_count[0] = color_count[1] = 0
        queue = []
        queue.append(i)
        color[i] = 0
        color_count[0] += 1
        while queue:
            if bipertite == False:
                break
            front_node = queue.pop()
            for child_node in range(0, len(graph[front_node])):
                if color[graph[front_node][child_node]] == -1:
                    color[graph[front_node][child_node]] = 1 - color[front_node]
                    queue.append(graph[front_node][child_node])
                    color_count[color[graph[front_node][child_node]]] += 1
                elif color[front_node] == color[graph[front_node][child_node]]:
                    bipertite = False
                    break
        if bipertite == False:
            print(0)
            break
        current = (pow_value[color_count[0]] + pow_value[color_count[1]]) % MOD
        result = result * current % MOD
    if bipertite:
        print(result)
    t -= 1
