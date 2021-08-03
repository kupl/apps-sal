import sys
import collections


n, m, k = list(map(int, str.split(sys.stdin.readline())))
if k == 0:

    print(-1)

else:

    d = collections.defaultdict(set)
    for _ in range(m):

        u, v, l = list(map(int, str.split(sys.stdin.readline())))
        d[u].add((v, l))
        d[v].add((u, l))

    aks = set(map(int, str.split(sys.stdin.readline())))
    cheapest = None
    for source in aks:

        for destination, l in d[source]:

            if destination not in aks:

                if cheapest is None:

                    cheapest = l

                else:

                    cheapest = min(cheapest, l)

    print(cheapest or -1)
