n, m, s, f = list(map(int, input().split()))
d = {}
for i in range(m):
    t, l, r = list(map(int, input().split()))
    d[t] = [l, r]
ans = ""
for i in range(1, n + m):
    if(s == f):
        print(ans)
        return
    t = -1
    if(f < s):
        t = s - 1
    else:
        t = s + 1
    if i in d:
        if((d[i][0] <= s and s <= d[i][1]) or (d[i][0] <= t and t <= d[i][1])):
            t = -1
    if(t == -1):
        ans += "X"
    else:
        if(f < s):
            ans += "L"
        else:
            ans += "R"
        s = t
print(ans)
