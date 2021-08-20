import collections
(n, m) = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
(g, r) = map(int, input().split())
q = collections.deque()
q.append((0, 0, 0))
checked = [[-1] * g for _ in range(m)]
checked[0][0] = 0
while len(q) != 0:
    (v, t, cnt) = q.popleft()
    if v != m - 1:
        cost1 = arr[v + 1] - arr[v]
        if t + cost1 <= g:
            if checked[v + 1][(t + cost1) % g] == -1:
                if t + cost1 < g:
                    q.appendleft((v + 1, t + cost1, cnt))
                    checked[v + 1][t + cost1] = cnt
                else:
                    q.append((v + 1, 0, cnt + 1))
                    checked[v + 1][0] = cnt + 1
    if v != 0:
        cost2 = arr[v] - arr[v - 1]
        if t + cost2 <= g:
            if checked[v - 1][(t + cost2) % g] == -1:
                if t + cost2 < g:
                    q.appendleft((v - 1, t + cost2, cnt))
                    checked[v - 1][t + cost2] = cnt
                else:
                    q.append((v - 1, 0, cnt + 1))
                    checked[v - 1][0] = cnt + 1
ans = 10 ** 18
for i in range(m):
    for j in range(g):
        if checked[i][j] == -1:
            continue
        elif j + n - arr[i] <= g:
            ans = min(ans, checked[i][j] * (g + r) + j + n - arr[i])
if ans == 10 ** 18:
    print(-1)
else:
    print(ans)
