from sys import stdin, stdout
(n, m) = stdin.readline().strip().split(' ')
(n, m) = (int(n), int(m))
adj_li = [[] for i in range(n + 1)]
for i in range(m):
    (u, v) = stdin.readline().strip().split(' ')
    (u, v) = (int(u), int(v))
    adj_li[u].append(v)
    adj_li[v].append(u)
visited = [False for i in range(n + 1)]
ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        flag = True
        q = [(i, -1)]
        visited[i] = True
        for (curr, par) in q:
            for i in adj_li[curr]:
                if i != par:
                    if not visited[i]:
                        q.append((i, curr))
                        visited[i] = True
                    else:
                        flag = False
        if flag:
            ans += 1
stdout.write(str(ans))
