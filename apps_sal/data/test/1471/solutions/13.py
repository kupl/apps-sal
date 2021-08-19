n = int(input())
uv = [[] for _ in range(n + 1)]
for i in range(n - 1):
    (u, v, w) = map(int, input().split())
    uv[u].append([v, w])
    uv[v].append([u, w])
stack = [1]
ans = [-1] * (n + 1)
ans[1] = 0
while stack:
    x = stack.pop()
    for (j, k) in uv[x]:
        if ans[j] == -1:
            if k % 2 == 0:
                ans[j] = ans[x]
            else:
                ans[j] = (ans[x] + 1) % 2
            stack.append(j)
for m in range(n):
    print(ans[m + 1])
