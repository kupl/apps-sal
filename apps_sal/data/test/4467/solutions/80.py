import sys
sys.setrecursionlimit(10 ** 8)


def ii():
    return int(sys.stdin.readline())


def mi():
    return map(int, sys.stdin.readline().split())


def li():
    return list(map(int, sys.stdin.readline().split()))


def li2(N):
    return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def dp2(ini, i, j):
    return [[ini] * i for _ in range(j)]


'\nN = ii()\nA = li2(N)\nB = li2(N)\n\nA = sorted(A, key=lambda x:x[0])\nB = sorted(B, key=lambda x:x[0])\n\na_ind = 0\nb_ind = 0\ncnt = 0\n\nwhile b_ind < N:\n    if A[a_ind][0] < B[b_ind][0] and  A[a_ind][1] < B[b_ind][1]:\n        cnt += 1\n        a_ind += 1\n        b_ind += 1\n    else:\n        b_ind += 1\n\nprint(cnt)\n'
'\n#nonlocal ans\nans = 0\n\ndef dfs(a_ind, b_ind, cnt):\n    if a_ind >= N or b_ind >= N:\n        nonlocal ans\n        ans = max(ans, cnt)\n        return\n    if A[a_ind][0] < B[b_ind][0] and  A[a_ind][1] < B[b_ind][1]:\n        dfs(a_ind+1, b_ind+1, cnt+1)\n    else:\n        dfs(a_ind+1, b_ind, cnt)\n        dfs(a_ind, b_ind+1, cnt)\n        dfs(a_ind+1, b_ind+1, cnt)\n\ndfs(0, 0, 0)\n\nprint(ans)\n'


def dfs(v, visited):
    """
    :param v: X側の未マッチングの頂点の1つ
    :param visited: 空のsetを渡す（外部からの呼び出し時）
    :return: 増大路が見つかればTrue
    """
    for u in edges[v]:
        if u in visited:
            continue
        visited.add(u)
        if matched[u] == -1 or dfs(matched[u], visited):
            matched[u] = v
            return True
    return False


N = ii()
xn = N
yn = N
edges = [set() for _ in range(xn)]
matched = [-1] * yn
A = li2(N)
B = li2(N)
for i in range(N):
    for j in range(N):
        if A[i][0] < B[j][0] and A[i][1] < B[j][1]:
            edges[i].add(j)
print(sum((dfs(s, set()) for s in range(xn))))
