from collections import deque

n = int(input())
m = n * (n - 1) // 2
b = [[0, 0] for _ in range(m + 1)]
f = [0] * (m + 1)
q = deque()
for i in range(1, n + 1):
    a = list(map(int, input().split()))
    for j in range(n - 1):
        ma, mi = max(i, a[j]), min(i, a[j])
        x = (ma - 1) * (ma - 2) // 2 + mi
        if j == 0:
            f[x] += 1
            if f[x] == 2:
                q.append(x)
        else:
            if b[y][0] == 0:
                b[y][0] = x
            else:
                b[y][1] = x
        y = x
ans = 0
while q:
    ans += 1
    l = len(q)
    for _ in range(l):
        i = q.popleft()
        for j in range(2):
            k = b[i][j]
            f[k] += 1
            if f[k] == 2 and not k == 0:
                q.append(k)
print(ans if f[0] == n else -1)
