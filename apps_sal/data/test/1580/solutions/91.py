import sys
sys.setrecursionlimit(10**9)
n, m = map(int, input().split())

rel = [[] for _ in range(n)]
for i in range(m):
    x, y, z = map(int, input().split())
    rel[x - 1].append(y - 1)
    rel[y - 1].append(x - 1)

ans = [-1] * n


def hoge(parent, pos):
    for i in rel[pos]:
        if ans[i] >= 0:
            continue
        ans[i] = pos
        hoge(pos, i)
    return


cnt = 0
for i in range(n):
    if ans[i] < 0:
        hoge(0, i)
        cnt += 1

print(cnt)
