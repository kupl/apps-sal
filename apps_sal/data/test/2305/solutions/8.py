import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n = int(input())
C = list(map(int, input().split()))


path = [set() for _ in range(n)]

for i in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    path[a].add(b)
    path[b].add(a)

ans = [n * (n + 1) // 2] * n
cparent = [[] for _ in range(n)]
root_size = [n] * n
reached = [False] * n
size = [0] * n


def dfs(p):
    c = C[p] - 1
    cparent[c].append(p)
    s = 1
    for nxt in path[p]:
        if reached[nxt]:
            continue
        reached[nxt] = True
        size[p] = 0
        ret = dfs(nxt)
        s += ret
        size[p] += ret
        ans[c] -= size[p] * (size[p] + 1) // 2
    cparent[c].pop()
    if cparent[c]:
        size[cparent[c][-1]] -= s
    else:
        root_size[c] -= s
    return s


reached = [False] * n
reached[0] = True

dfs(0)
for i in range(n):
    print((ans[i] - root_size[i] * (root_size[i] + 1) // 2))
