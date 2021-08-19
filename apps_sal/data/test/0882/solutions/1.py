def prefix(st):
    t = 0
    p = [0] * (len(st) + 1)
    o = [0] * (len(st) + 1)
    for i in range(2, len(st)):
        while t > 0 and st[i] != st[t + 1]:
            t = p[t]
        if st[i] == st[t + 1]:
            t += 1
        p[i] = t
    while t > 0:
        o[t] = 1
        t = p[t]
    return o


s = ' ' + input()
t = ' ' + input()
o = prefix(t)
m = len(t) - 1
ans = [[0, 0] for _ in range(len(s) + 5)]
ans[0][1] = float('-inf')
for i in range(1, len(s)):
    j = m
    ans[i][1] = float('-inf')
    for j in range(m, 0, -1):
        if s[i - m + j] != '?' and s[i - m + j] != t[j]:
            break
        if o[j - 1]:
            ans[i][1] = max(ans[i][1], ans[i - m + j - 1][1] + 1)
        if j == 1:
            ans[i][1] = max(ans[i][1], ans[i - m][0] + 1)
    ans[i][0] = max(ans[i][1], ans[i - 1][0])
if ans[len(s) - 1][0] == 7:
    print(o.count(1))
else:
    print(ans[len(s) - 1][0])
