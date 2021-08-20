def edmonds_karp(s, t, C):
    """
    s, t: start, target (integer)
    C: Array of dict ([from][to] -> length)
    ret: maximum_flow (integer)
    """
    import copy
    import collections
    r = copy.deepcopy(c)
    maxf = 0
    while True:
        (q, found) = (collections.deque(), False)
        q.append(([s], 10 ** 15))
        while len(q) > 0 and (not found):
            (p, minf) = q.popleft()
            for (to, flow) in list(r[p[-1]].items()):
                if flow == 0:
                    continue
                elif to == t:
                    (p, minf) = (p + [to], min(flow, minf))
                    found = True
                    break
                elif not to in p:
                    q.append((p + [to], min(flow, minf)))
        if not found:
            break
        for i in range(len(p) - 1):
            r[p[i]][p[i + 1]] -= minf
            if p[i] in r[p[i + 1]]:
                r[p[i + 1]][p[i]] += minf
            else:
                r[p[i + 1]][p[i]] = minf
        maxf += minf
    return maxf


N = int(input())
A = list(map(int, input().split()))
gain = sum([max(a, 0) for a in A])
(S, T) = (0, N + 1)
c = [{} for i in range(N + 2)]
for i in range(N):
    ix = i + 1
    if A[i] <= 0:
        c[S][ix] = -A[i]
    else:
        c[ix][T] = A[i]
    for j in range(2 * ix, N + 1, ix):
        c[ix][j] = 10 ** 15
print(gain - edmonds_karp(S, T, c))
