import sys
input = sys.stdin.readline
(n, m) = map(int, input().split())
eins = set()
for _ in range(m):
    (v, to) = map(int, input().split())
    eins.add((v, to))
    eins.add((to, v))
notVisited = set(range(1, n + 1))
comps = []
for s in range(1, n + 1):
    if s in notVisited:
        notVisited.remove(s)
        ctr = 1
        stack = [s]
        while stack:
            v = stack.pop()
            visited = set()
            for to in notVisited:
                if (v, to) not in eins:
                    visited.add(to)
                    stack.append(to)
                    ctr += 1
            notVisited -= visited
        comps.append(ctr)
comps.sort()
print(len(comps))
print(*comps)
