import sys

BigNum = 10 ** 10

class DSU:
    def __init__(self, count, stateInitializer, stateMerger):
        self.vs = list(range(count))
        self.states = [stateInitializer(i) for i in range(count)]
        self.sizes = [1] * count
        self.merger = stateMerger
    
    def get(self, i):
        if self.vs[i] == i:
            return i
        else:
            res = self.get(self.vs[i])
            self.vs[i] = res
            return res

    def getState(self, i):
        return self.states[self.get(i)]
    
    def setState(self, i, newState):
        i = self.get(i)
        self.states[i] = newState
    
    def unite(self, a, b):
        a = self.get(a)
        b = self.get(b)
        if a == b:
            return a

        mergedState = self.merger(self.states[a], self.states[b])
        if self.sizes[a] >= self.sizes[b]:
            self.vs[b] = a
            self.sizes[a] += self.sizes[b]
            self.states[a] = mergedState
            return a
        else:
            self.vs[a] = b
            self.sizes[b] += self.sizes[a]
            self.states[b] = mergedState
            return b
    
    def flatten(self):
        for i in range(len(self.vs)):
            self.get(i)
    
    def setNames(self):
        self.flatten()
        return set(self.vs)

n, m, s = list(map(int, input().split(' ')))
ps = [[] for _ in range(n+1)]
edges = []
for i in range(m):
    u, v = list(map(int, input().split(' ')))
    ps[v] += [u]
    edges += [(u, v)]

dsu = DSU(
    n+1,
    lambda i: (0, BigNum),
    lambda a, b: (min(a[0], b[0]), min(a[1], b[1]))
)

def dfs(v, depth):
    vSt = dsu.getState(v)
    vState, vMinDepth = vSt

    if vState >= 1:
        raise 'Not supposed to dfs processed node!'

    vState = 1
    vMinDepth = depth
    dsu.setState(v, (vState, vMinDepth))

    for nv in ps[v]:
        #print(':', v, nv)
        nvSt = dsu.getState(nv)
        nvState, nvMinDepth = nvSt

        if nvState == 2:
            continue
        if nvState == 1:
            if nvMinDepth < vMinDepth:
                vMinDepth = nvMinDepth
                dsu.setState(v, (vState, vMinDepth))
        else:
            nvMinDepth = dfs(nv, depth + 1)
            if nvMinDepth <= depth:
                dsu.unite(v, nv)

            if nvMinDepth < vMinDepth:
                vMinDepth = nvMinDepth
                dsu.setState(v, (vState, vMinDepth))

    if depth <= vMinDepth:
        vState = 2
        dsu.setState(v, (vState, vMinDepth))

    return vMinDepth


sys.setrecursionlimit(12000)

for i in range(1, n+1):
    st = dsu.getState(i)
    if st[0] == 0:
        dfs(i, 0)

components = dsu.setNames().difference({0})
#print(dsu.vs)
#print(components)

components = components.difference({ dsu.get(s) })
for (u, v) in edges:
    u, v = dsu.get(u), dsu.get(v)
    if u == v:
        continue
    components = components.difference({ v })

#print(components)
print(len(components))

