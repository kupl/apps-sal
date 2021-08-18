from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append(b)
    d[b].append(a)
vis = [0] * n
for i in range(n):
    if vis[i] == 0:
        q = [i]
        ce = 0
        cv = 0
        vis[i] = 1
        while q:
            t = q.pop()
            cv += 1
            ce += len(d[t])
            for i in d[t]:
                if not vis[i]:
                    vis[i] = 1
                    q.append(i)
    if ce != cv * (cv - 1):
        print('NO')
        return
print('YES')
