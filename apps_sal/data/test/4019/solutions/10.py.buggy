import sys
from collections import Counter, defaultdict


def i_ints():
    return map(int, sys.stdin.readline().split())


n, m, D = i_ints()
E = defaultdict(set)
for i in range(m):
    u, v = i_ints()
    E[u].add(v)
    E[v].add(u)


def append_edge(u, v):
    E[u].discard(v)
    E[v].discard(u)
    t.add(u)
    t.add(v)
    te.append((u, v))


def complete_tree(u):
    nonlocal too_much
    todo = {u}
    while todo:
        u = todo.pop()
        for v in list(E[u]):
            if v not in t:
                if v not in starts:
                    append_edge(u, v)
                    todo.add(v)
                else:
                    if too_much > 0:
                        append_edge(u, v)
                        todo.add(v)
                        too_much -= 1


def print_tree():
    for u, v in te:
        print(u, v)


u0 = 1
t = {u0}
te = []
starts = set(E[u0])
too_much = len(starts) - D
if too_much >= 0:
    for v in starts:
        if v not in t:
            append_edge(u0, v)
            complete_tree(v)
if not too_much:
    print("YES")
    print_tree()
else:
    print("NO")
