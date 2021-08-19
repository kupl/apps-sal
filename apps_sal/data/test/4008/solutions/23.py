(q, w) = list(map(int, input().split()))
a = list(map(int, input().split()))
s = []
d = []
ans = []
b = True
for i in a:
    if i in s:
        k = s.index(i)
        d[k] += 1
        ans.append(d[k])
    else:
        s.append(i)
        ans.append(1)
        d.append(1)
j = max(ans)
if j > w:
    print('NO')
else:
    l = 1
    i = j + 1
    while i < w + 1:
        while ans.count(l) == 1:
            l += 1
        h = ans.count(l)
        while (i < w + 1) & (h > 1):
            f = ans.index(l)
            ans = ans[:f] + [i] + ans[f + 1:]
            i += 1
            h -= 1
    print('YES')
    print(*ans)
