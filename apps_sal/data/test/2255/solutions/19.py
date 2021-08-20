import heapq
import sys


def __starting_point():
    path = dict()
    input()
    for line in sys.stdin:
        if line.strip() == '':
            break
        (n, m) = [int(i) for i in line.strip().split()]
        if n not in path:
            path[n] = [m]
        else:
            path[n].append(m)
        if m not in path:
            path[m] = [n]
        else:
            path[m].append(n)
    ans = [1]
    visited = set([1])
    pq = path[1]
    heapq.heapify(pq)
    while len(pq) > 0:
        the_next = heapq.heappop(pq)
        if the_next not in visited:
            ans.append(the_next)
            visited.add(the_next)
            for i in path[the_next]:
                heapq.heappush(pq, i)
    print(' '.join([str(i) for i in ans]))


__starting_point()
