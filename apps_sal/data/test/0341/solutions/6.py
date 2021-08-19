from collections import deque
(n, k) = map(int, input().split())
(r, s, p) = map(int, input().split())
t = input()
d = {'s': r, 'p': s, 'r': p}
before = deque([])
ans = 0
for i in range(n):
    if i < k:
        before.append(t[i])
        ans += d[t[i]]
    else:
        b = before.popleft()
        if t[i] != b:
            before.append(t[i])
            ans += d[t[i]]
        else:
            before.append('n')
print(ans)
