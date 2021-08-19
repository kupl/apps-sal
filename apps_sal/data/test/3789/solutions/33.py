import copy
import collections

N = int(input())
A = list(map(int, input().split()))

gain = sum([max(a, 0) for a in A])

# Flow network
S, T = 0, N + 1
c = [{} for i in range(N + 2)]
for i in range(N):
    ix = i + 1
    if A[i] <= 0:
        c[S][ix] = -A[i]
    else:
        c[ix][T] = A[i]

    for j in range(2 * ix, N + 1, ix):
        c[ix][j] = 10e15

# Residual network
r = copy.deepcopy(c)

# Edmonds-Karp algorithm
max_flow = 0
while True:
    # Find path to T
    q, s, p = collections.deque(), {S}, None
    q.append((S,))
    findPath = False
    while not len(q) == 0 and not findPath:
        cand_path = q.popleft()
        for to, path in list(r[cand_path[-1]].items()):
            if path == 0:
                continue
            elif to == T:
                p = cand_path + (to,)
                findPath = True
            elif not to in s:
                q.append(cand_path + (to,))
                s.add(to)

    if not findPath:
        break

    # Minimum flow
    min_flow = min([r[p[i]][p[i + 1]] for i in range(len(p) - 1)])
    max_flow += min_flow
    for i in range(len(p) - 1):
        r[p[i]][p[i + 1]] -= min_flow
        if p[i] in r[p[i + 1]]:
            r[p[i + 1]][p[i]] += min_flow
        else:
            r[p[i + 1]][p[i]] = min_flow

print((gain - max_flow))
