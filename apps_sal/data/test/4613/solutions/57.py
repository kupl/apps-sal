from networkx import *
(n, m) = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
g = Graph(a)
print(len(tuple(bridges(g))))
