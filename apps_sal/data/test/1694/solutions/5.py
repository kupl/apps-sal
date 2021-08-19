(n, m, s, f) = list(map(int, input().split()))
t = {}
step = 1
ans = ''
if s < f:
    sig = 'R'
else:
    sig = 'L'
for i in range(m):
    (t0, l0, r0) = list(map(int, input().split()))
    t[t0] = [l0, r0]
for i in range(1, n + m + 1):
    if s < f:
        u = s + 1
    else:
        u = s - 1
    if i in t:
        if t[i][0] <= s <= t[i][1] or t[i][0] <= u <= t[i][1]:
            ans += 'X'
        else:
            ans += sig
            s = u
    else:
        ans += sig
        s = u
    if s == f:
        break
print(ans)
