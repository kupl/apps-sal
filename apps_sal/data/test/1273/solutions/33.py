from collections import deque
n = int(input())
edges_ls = [[0, 0] for _ in range(n - 1)]
edges_d = {}
ver_ls = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges_d[(a, b)] = i
    edges_d[(b, a)] = i
    edges_ls[i] = [a, b]
    ver_ls[a].append(b)
    ver_ls[b].append(a)
n_color = 0
for ver in ver_ls:
    n_color = max(n_color, len(ver))


def next_color(color):
    return (color + 1) % n_color


edge_color = [0] * (n - 1)
q = deque()
color_now = 0
for ver in ver_ls[0]:
    q.append([0, ver, color_now])
    edge_color[edges_d[(0, ver)]] = color_now
    color_now = next_color(color_now)
done_ls = [0] * n
done_ls[0] = 1

while q:
    From, to, color_now = q.popleft()
    # verはtoからの行先
    for ver in ver_ls[to]:
        if not done_ls[ver]:
            q.append([to, ver, next_color(color_now)])
            edge_color[edges_d[(to, ver)]] = next_color(color_now)
            color_now = next_color(color_now)
    done_ls[to] = 1

print(n_color)
for color in edge_color:
    print(color + 1)
