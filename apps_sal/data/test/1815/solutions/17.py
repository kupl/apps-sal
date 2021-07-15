n = int(input())
apr, l, f, ans = 0, [0] * 100001, [0] * 100001, 1
i = 0
for x in input().split():
    x = int(x)
    if l[x] == 0:
        l[x] += 1
        apr += 1
        f[1] += 1
    else:
        f[l[x]] -= 1
        l[x] += 1
        f[l[x]] += 1

    if i % apr == 0:
        tmp = i // apr
        if f[tmp] == apr - 1:
            ans = max(ans, i + 1)

    if apr > 1 and i % (apr - 1) == 0:
        tmp = i // (apr - 1)
        if f[tmp] == apr - 1 or f[tmp] == apr:
            ans = max(ans, i + 1)
    i += 1
print(ans)

