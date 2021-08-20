(n, m) = list(map(int, input().split()))


def bellman_ford(s):
    d = [float('inf')] * n
    d[s] = 0
    for i in range(n * 2):
        for edge in g:
            if edge[0] != float('inf') and d[edge[1]] > d[edge[0]] + edge[2]:
                d[edge[1]] = d[edge[0]] + edge[2]
                if i >= n - 1 and edge[1] == n - 1:
                    return -1
    return d


g = []
for _ in range(m):
    (a, b, c) = list(map(int, input().split()))
    a -= 1
    b -= 1
    c *= -1
    g.append([a, b, c])
ret = bellman_ford(0)
if isinstance(ret, list):
    print(-1 * ret[n - 1])
else:
    print('inf')
