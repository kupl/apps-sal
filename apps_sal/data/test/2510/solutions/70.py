from collections import deque
(n, m) = map(int, input().split())
E = [[] for _ in range(n)]
for i in range(m):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)
flag = [True for _ in range(n)]
ans = 0
for i in range(n):
    if flag[i]:
        counter = 1
        flag[i] = False
        que = deque([i])
        while que:
            now = deque.popleft(que)
            for j in E[now]:
                if flag[j]:
                    deque.append(que, j)
                    counter += 1
                    flag[j] = False
        ans = max(ans, counter)
print(ans)
