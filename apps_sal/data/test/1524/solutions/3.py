s = input()
v = [0 for i in range(len(s))]
(r, l) = (0, 0)
vis = [False for i in range(len(s))]
for i in range(len(s)):
    if vis[i]:
        continue
    vis[i] = True
    if s[i] == 'L':
        x = i - 1
        y = i
        (r, l) = (0, 0)
        while x >= 0 and s[x] == 'R':
            r += 1
            x -= 1
        while y <= len(s) - 1 and s[y] == 'L':
            vis[y] = True
            l += 1
            y += 1
        v[i - 1] = l // 2 + (r - r // 2)
        v[i] = l - l // 2 + r // 2
print(*v)
