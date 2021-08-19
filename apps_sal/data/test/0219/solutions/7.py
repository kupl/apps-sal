(n, m, s, d) = map(int, input().split())
x = sorted(map(int, input().split())) + [m + s + 1]
cur = l = 0
ans = []
while l < m:
    r = min(x[cur] - 1, m)
    ans += ['RUN ' + str(r - l)]
    if r == m:
        break
    if r - l < s:
        ans = ['IMPOSSIBLE']
        break
    t = x[cur] + 1
    while x[cur + 1] - 1 - t < s:
        cur += 1
        t = x[cur] + 1
    if t - r > d:
        ans = ['IMPOSSIBLE']
        break
    ans += ['JUMP ' + str(t - r)]
    l = t
    cur += 1
print('\n'.join(ans))
