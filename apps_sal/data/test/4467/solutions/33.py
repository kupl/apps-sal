import collections
import itertools
import copy


class MaximumFlow:

    def ford_fulkerson(self, G, s, t):
        G_residue = copy.deepcopy(G)

        def dfs(start, used):
            if start == t:
                return [start]
            for (end, cap) in list(G_residue[start].items()):
                if cap > 0 and end not in used:
                    used.add(end)
                    ret = dfs(end, used)
                    if ret:
                        return ret + [start]
            return []
        flow_value = 0
        while True:
            root = dfs(s, set([s]))
            if root:
                root = root[::-1]
                residue = min([G_residue[a][b] for (a, b) in zip(root, root[1:])])
                flow_value += residue
                for (a, b) in zip(root, root[1:]):
                    G_residue[a][b] -= residue
                    G_residue[b][a] += residue
            else:
                return (flow_value, G_residue)


N = int(input())
AB = [[int(_) for _ in input().split()] for _ in range(N)]
CD = [[int(_) for _ in input().split()] for _ in range(N)]
G = collections.defaultdict(lambda: collections.defaultdict(int))
for (a, b) in AB:
    G[-1][1000 * a + b] = 1
for (c, d) in CD:
    G[1000 * c + d][-2] = 1
for (ab, cd) in itertools.product(AB, CD):
    (a, b) = ab
    (c, d) = cd
    if a < c and b < d:
        G[1000 * a + b][1000 * c + d] = 1
(flow_value, G_residue) = MaximumFlow().ford_fulkerson(G, -1, -2)
print(flow_value)
flow_dict = collections.defaultdict(lambda: collections.defaultdict(int))
for a in G:
    for b in G[a]:
        if G_residue[b][a] > 0:
            flow_dict[a][b] = G_residue[b][a]
