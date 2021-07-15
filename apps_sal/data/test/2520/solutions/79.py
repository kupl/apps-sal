from collections import deque

N, M, K = list(map(int, input().split()))
friend = [list(map(int, input().split())) for _ in range(M)]
block = [list(map(int, input().split())) for _ in range(K)]

f = [set() for _ in range(N + 1)]
b = [set() for _ in range(N + 1)]

for i, j in friend:
    f[i].add(j)
    f[j].add(i)
for i, j in block:
    b[i].add(j)
    b[j].add(i)

stack = deque()
ans = [0] * (N + 1)
visited = [0] * (N + 1)

for i in range(1, N + 1):
    if visited[i]:
        continue
    # setは{}で書く
    link = {i}
    stack.append(i)
    visited[i] = 1
    while stack:
        n = stack.pop()
        # nのフレンド全員について
        for j in f[n]:
            if visited[j] == 0:
                stack.append(j)
                visited[j] = 1
                # link(set)に追加
                link.add(j)
    for i in link:
        # 全体-既にフレンドの人数-ブロックした人数-自分自身
        # set同士で積集合をとる
        ans[i] = len(link) - len(link & f[i]) - len(link & b[i]) - 1

print((*ans[1:]))

