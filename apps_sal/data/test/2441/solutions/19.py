import sys
read = lambda f=int: list(map(f, sys.stdin.readline().split()))
array = lambda *ds: [array(*ds[1:]) for _ in range(ds[0])] if ds else 0

def main():
    N, = read()
    cost = tuple(read())
    E, = read()
    es = [tuple(read()) for _ in range(E)]

    class Node:
        def __init__(self, name):
            self.name = name
            self.index = None
            self.lowlink = None
            self.adj = []
            self.on_stack = False

    vs = [Node(i) for i in range(N)]
    for v, w in es:
        vs[v-1].adj.append(vs[w-1])

    i = 0
    stack = []
    call_stack = []
    comps = []
    for v in vs:
        if v.index is None:
            call_stack.append((v,0))
            while call_stack:
                v, pi = call_stack.pop()
                if pi == 0:
                    v.index = i
                    v.lowlink = i
                    i += 1
                    stack.append(v)
                    v.on_stack = True
                # If we just recursed on something
                if pi > 0:
                    prev = v.adj[pi-1]
                    v.lowlink = min(v.lowlink, prev.lowlink)
                # Find the next thing to recurse on
                while pi < len(v.adj) and v.adj[pi].index is not None:
                    w = v.adj[pi]
                    if w.on_stack:
                        v.lowlink = min(v.lowlink, w.index)
                    pi += 1
                # If we found something with index=None, recurse
                if pi < len(v.adj):
                    w = v.adj[pi]
                    assert w.index is None
                    call_stack.append((v,pi+1))
                    call_stack.append((w,0))
                    continue
                if v.lowlink == v.index:
                    comp = []
                    while True:
                        w = stack.pop()
                        w.on_stack = False # This is important, since later nodes may see it
                        comp.append(w.name)
                        if w is v:
                            break
                    comps.append(comp)

    #print(stack)
    #print(comps)
    res = 0
    ways = 1
    for comp in comps:
        c = min(cost[v] for v in comp)
        res += c
        ways *= sum(1 for v in comp if cost[v] == c)
        ways %= 10**9 + 7
    print(res, ways)

main()

