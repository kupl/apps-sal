import sys
input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))


def neighbours(node, s=S):
    out = [node << 1]
    if node % 3 == 0:
        out.append(node // 3)
    return set((x for x in out if x in s))


G = {}
for x in S:
    G[x] = neighbours(x)


def hamilton(G, size, pt, path=None):
    if path == None:
        path = []
    if pt not in set(path):
        path.append(pt)
        if len(path) == size:
            return path
        for pt_next in G.get(pt, []):
            res_path = [i for i in path]
            candidate = hamilton(G, size, pt_next, res_path)
            if candidate is not None:
                return candidate


for x in S:
    P = hamilton(G, N, x)
    if P:
        print(' '.join(map(str, P)))
        break
