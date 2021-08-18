import sys


def line():
    return sys.stdin.readline()


def numbers():
    return list(map(int, line().split()))


def number():
    return int(line())


adjlist = {}
n, k = 0, 0
mark = [False] * 2010
edges = [False] * 1010


def bfs(s):

    i = 0
    frontier = [s]
    while frontier:

        if mark[s]:
            break

        next_frontier = []
        for u in frontier:

            for v, isState in enumerate(edges):
                if isState:
                    state = u + (n - 1000) - v

                    if state >= 0 and state <= 2000 and not mark[state]:
                        mark[state] = True
                        next_frontier.append(state)

        frontier = next_frontier
        i += 1

    if mark[s]:
        return i
    else:
        return -1


[n, k] = numbers()
concentrations = numbers()

for x in concentrations:
    edges[x] = True

n = n + 1000
ans = bfs(1000)
print(ans)
