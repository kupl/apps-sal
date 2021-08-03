import sys
sys.setrecursionlimit(10**7)
n, m = list(map(int, input().split()))
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = list(map(int, input().split()))
    u, v = u - 1, v - 1
    g[u].append(v)
mi = set(range(n))
flg = False


def func(path):
    chk = set(path)
    if len(path) != 2:
        for i, v in enumerate(path):
            nvs = [nv for nv in g[v] if nv in chk]
            if len(nvs) == 1:
                continue
            for nv in nvs:
                if nv == path[(i + 1) % len(path)]:
                    continue
                ary = [nv]
                for j, vj in enumerate(path):
                    if vj == nv:
                        break
                if i > j:
                    ary = path[j:i + 1]
                else:
                    ary = path[:i + 1] + path[j:]
                # print(path,ary,i,j)
                func(ary)
    print((len(path)))
    for v in path:
        print((v + 1))
    return


def dfs(v, seen):
    mi.discard(v)
    for nv in g[v]:
        if seen[nv] != -1:  # 巡回閉路
            seen[nv] = v
            path = [v]
            chk = {v}
            while seen[v] not in chk:
                v = seen[v]
                path.append(v)
                chk.add(v)
            path.reverse()
            func(path)
        else:
            seen[nv] = v
            dfs(nv, seen)
            seen[nv] = -1


while mi:
    v = mi.pop()
    seen = [-1] * n
    dfs(v, seen)
print((-1))
return
