def get():
    return list(map(int, input().split()))


def dfs(i):
    v = c[i]
    q = [i]
    while q:
        j = q.pop()
        b[j] = 1
        v = min(v, c[j])
        for k in a[j]:
            if b[k] == 0:
                q.append(k)
    return v


(n, m) = get()
c = get()
a = [list() for _ in range(n)]
for _ in range(m):
    (x, y) = get()
    a[x - 1].append(y - 1)
    a[y - 1].append(x - 1)
b = [0] * n
ans = 0
for i in range(n):
    if b[i] == 0:
        ans += dfs(i)
print(ans)
