def main():
    from itertools import combinations
    n = int(input())
    ab = [tuple(sorted(list(map(int, input().split())))) for _ in [0] * (n - 1)]
    m = int(input())
    uv = [list(map(int, input().split())) for _ in [0] * m]
    g = [[] for _ in [0] * n]
    [g[a - 1].append(b - 1) for a, b in ab]
    [g[b - 1].append(a - 1) for a, b in ab]

    d = dict()
    for i, (a, b) in enumerate(ab):
        d[(a - 1, b - 1)] = i

    def tree_path(root, goal):
        d = [-1] * n  # 根からの距離
        d[root] = 0
        q = [root]
        cnt = 0
        while q:  # BFS
            cnt += 1
            qq = []
            while q:
                i = q.pop()
                for j in g[i]:
                    if d[j] == -1:
                        d[j] = cnt
                        qq.append(j)
            q = qq
        now = goal
        path = [goal]
        while True:
            dist = d[now]
            for i in g[now]:
                if d[i] < dist:
                    now = i
                    path.append(i)
                    break
            if dist == 1:
                break
        return path

    seiyaku = [set() for _ in [0] * m]

    for i, (u, v) in enumerate(uv):
        path = tree_path(u - 1, v - 1)
        for j in range(len(path) - 1):
            x, y = min(path[j], path[j + 1]), max(path[j], path[j + 1])
            seiyaku[i].add(d[(x, y)])

    cnt = 2**(n - 1)

    for i in range(1, m + 1):
        flag = 1
        if i % 2 == 1:
            flag = -1
        cc = combinations(list(range(m)), i)
        for c in cc:
            s = set()
            for j in c:
                s |= seiyaku[j]
            cnt += (2**(n - 1 - len(s))) * flag
    print(cnt)


main()
