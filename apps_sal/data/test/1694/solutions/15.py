(n, m, s, f) = list(map(int, input().split()))
l = []
for i in range(m):
    k = list(map(int, input().split()))
    l.append(k)
count = 1
ans = ''
i = 0
while i < m:
    if count < l[i][0]:
        if f > s:
            ans += 'R' * min(l[i][0] - count, f - s)
            s += min(l[i][0] - count, f - s)
            count = l[i][0]
        if f < s:
            ans += 'L' * min(l[i][0] - count, s - f)
            s -= min(l[i][0] - count, s - f)
            count = l[i][0]
    else:
        if l[i][1] <= s <= l[i][2]:
            ans += 'X'
        else:
            if f > s:
                if l[i][1] <= s + 1 <= l[i][2]:
                    ans += 'X'
                else:
                    ans += 'R'
                    s += 1
            if f < s:
                if l[i][1] <= s - 1 <= l[i][2]:
                    ans += 'X'
                else:
                    ans += 'L'
                    s -= 1
        i += 1
        count += 1
    if s == f:
        break
if s != f:
    if s < f:
        ans += 'R' * (f - s)
    else:
        ans += 'L' * (s - f)
print(ans)
