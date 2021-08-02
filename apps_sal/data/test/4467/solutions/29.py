import collections
import itertools


class MaximumFlow:
    def __init__(self, G):
        self.G = G

    def ford_fulkerson(self, s, t):
        def dfs(start, used):
            G = self.G
            if start == t:
                return [start]
            for end, cap in list(G[start].items()):
                if cap > 0 and end not in used:
                    used.add(end)
                    ret = dfs(end, used)
                    if ret:
                        return ret + [start]
            return []

        fmax = 0
        cnt = 0
        while True:
            G = self.G
            cnt += 1
            root = dfs(s, set([s]))
            if root:
                root = root[::-1]
                residue = min([G[a][b] for a, b in zip(root, root[1:])])
                fmax += residue
                for a, b in zip(root, root[1:]):
                    G[a][b] -= residue
                    G[b][a] += residue
            else:
                return (fmax, G)


N = int(input())
AB = [[int(_) for _ in input().split()] for _ in range(N)]
CD = [[int(_) for _ in input().split()] for _ in range(N)]
G = collections.defaultdict(lambda: collections.defaultdict(int))
for a, b in AB:
    G[-1][1000 * a + b] = 1
for c, d in CD:
    G[1000 * c + d][-2] = 1
for ab, cd in itertools.product(AB, CD):
    a, b = ab
    c, d = cd
    if a < c and b < d:
        G[1000 * a + b][1000 * c + d] = 1
flow = MaximumFlow(G)
fmax, Gres = flow.ford_fulkerson(-1, -2)
print(fmax)
