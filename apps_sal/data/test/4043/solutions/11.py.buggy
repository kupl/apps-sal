from collections import deque
n, d, k = map(int, input().split())
if n == 1:
    print('NO')
    return
if n == 2:
    if d > 1:
        print('NO')
    else:
        print('YES')
        print(1, 2)
    return
if (not 2 <= d <= n - 1) or k == 1:
    print('NO')
    return
ans = []
for i in range(d):
    ans.append((i + 1, i + 2))
now = d + 2
for i in range(d - 1):
    q = deque([(i + 2, min(i, d - i - 2))])
    first = True
    while q and len(ans) < n - 1:
        node, depth = q.popleft()
        end = now + k - 1
        if first:
            end -= 1
        for j in range(now, end):
            ans.append((node, j))
            if len(ans) == n - 1:
                break
            if depth > 0:
                q.append((j, depth - 1))
        now = end
        first = False

if len(ans) == n - 1:
    print('YES')
    for i, j in ans:
        print(i, j)
else:
    print('NO')
