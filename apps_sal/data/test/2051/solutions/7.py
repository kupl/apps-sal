import sys
n, m, k = [int(x) for x in sys.stdin.readline().replace('\n', '').split(' ')]
c = [int(x) for x in sys.stdin.readline().replace('\n', '').split(' ')]
socks = [[] for _ in range(n)]
for i in range(m):
    l, r = [int(x) - 1 for x in sys.stdin.readline().replace('\n', '').split(' ')]
    socks[r] += [l]
    socks[l] += [r]
visited = [False for _ in range(n)]
forest = {}
for i, v in enumerate(visited):
    if v:
        continue
    visited[i] = True
    queue = [(i, i)]
    forest[i] = {'nodes': 1, 'colours': {c[i]: 1}}
    while len(queue) != 0:
        representant, current = queue.pop()
        for node in socks[current]:
            if not visited[node]:
                queue += [(representant, node)]
                forest[representant]['nodes'] += 1
                if c[node] in forest[representant]['colours']:
                    forest[representant]['colours'][c[node]] += 1
                else:
                    forest[representant]['colours'][c[node]] = 1
                visited[node] = True
total = 0
for key in forest:
    maximun = 0
    for i in forest[key]['colours']:
        if forest[key]['colours'][i] > maximun:
            maximun = forest[key]['colours'][i]
    total += forest[key]['nodes'] - maximun
sys.stdout.write(str(total))
