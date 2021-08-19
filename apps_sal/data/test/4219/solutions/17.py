n = int(input())
(ans, a, l) = (0, [], [])
for i in range(n):
    a.append(int(input()))
    l.append([])
    for j in range(a[-1]):
        l[i].append(list(map(int, input().split())))
for i in range(2 ** n):
    (c, skip) = ([0] * n, False)
    for j in range(n):
        if i >> j & 1:
            c[j] = 1
    for j in range(n):
        if c[j] == 1:
            for k in range(a[j]):
                if c[l[j][k][0] - 1] != l[j][k][1]:
                    skip = True
                    break
        if skip:
            break
    else:
        ans = max(ans, sum(c))
print(ans)
