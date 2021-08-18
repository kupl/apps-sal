import sys
def read(f=int): return list(map(f, sys.stdin.readline().split()))


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
        vs[v - 1].adj.append(vs[w - 1])

    def scc(vs):
        i = 0
        stack = []
        call_stack = []
        comps = []
        for v in vs:
            if v.index is None:
                call_stack.append((v, 0))
                while call_stack:
                    v, pi = call_stack.pop()
                    if pi == 0:
                        v.index = i
                        v.lowlink = i
                        i += 1
                        stack.append(v)
                        v.on_stack = True
                    if pi > 0:
                        prev = v.adj[pi - 1]
                        v.lowlink = min(v.lowlink, prev.lowlink)
                    while pi < len(v.adj) and v.adj[pi].index is not None:
                        w = v.adj[pi]
                        if w.on_stack:
                            v.lowlink = min(v.lowlink, w.index)
                        pi += 1
                    if pi < len(v.adj):
                        w = v.adj[pi]
                        call_stack.append((v, pi + 1))
                        call_stack.append((w, 0))
                        continue
                    if v.lowlink == v.index:
                        comp = []
                        while True:
                            w = stack.pop()
                            w.on_stack = False
                            comp.append(w.name)
                            if w is v:
                                break
                        comps.append(comp)
        return comps

    def scc2(vs):
        result = []
        stack = []
        low = {}
        graph = {v.name: [w.name for w in v.adj] for v in vs}

        def visit(node):
            if node in low:
                return

            num = len(low)
            low[node] = num
            stack_pos = len(stack)
            stack.append(node)

            for successor in graph[node]:
                visit(successor)
                low[node] = min(low[node], low[successor])

            if num == low[node]:
                component = tuple(stack[stack_pos:])
                del stack[stack_pos:]
                result.append(component)
                for item in component:
                    low[item] = len(graph)

        for v in graph:
            visit(v)

        return result

    def scc3(vs):
        graph = {v.name: [w.name for w in v.adj] for v in vs}
        result = []
        stack = []
        low = {}
        call_stack = []

        for v in graph:
            call_stack.append((v, 0, len(low)))
            while call_stack:
                v, pi, num = call_stack.pop()
                if pi == 0:
                    if v in low:
                        continue
                    low[v] = num
                    stack.append(v)
                if pi > 0:
                    low[v] = min(low[v], low[graph[v][pi - 1]])
                if pi < len(graph[v]):
                    call_stack.append((v, pi + 1, num))
                    call_stack.append((graph[v][pi], 0, len(low)))
                    continue
                if num == low[v]:
                    comp = []
                    while True:
                        comp.append(stack.pop())
                        low[comp[-1]] = len(graph)
                        if comp[-1] == v:
                            break
                    result.append(comp)

        return result

    res = 0
    ways = 1
    for comp in scc3(vs):
        c = min(cost[v] for v in comp)
        res += c
        ways *= sum(1 for v in comp if cost[v] == c)
        ways %= 10**9 + 7
    print(res, ways)


main()
