def common(l1, l2):
    for i in range(3):
        for j in range(3):
            if l1[i] == l2[j]:
                return l1[i]
    return 0


def comp(l1, a, b):
    for i in l1:
        if i != a and i != b:
            return i


n = int(input())
l = []
d = {}
commons = {}
for i in range(n - 2):
    l.append(list(map(int, input().split())))
for i in range(n - 2):
    for j in l[i]:
        if j in d:
            d[j].append(i)
        else:
            d[j] = [i]
start = -1
end = -1
for i in d:
    if len(d[i]) == 1:
        if start == -1:
            start = i
            startg = d[i][0]
        else:
            end = i
            endg = d[i][0]
            break
for i in l[startg]:
    if len(d[i]) == 2:
        second = i
        break
for i in l[endg]:
    if len(d[i]) == 2:
        seclast = i
        break
i = 1
ans = [-1] * n
ans[0] = start
ans[1] = second
ans[n - 1] = end
ans[n - 2] = seclast
if ans[i - 1] in l[d[ans[i]][0]]:
    ans[i + 1] = comp(l[d[ans[i]][0]], ans[i - 1], ans[i])
elif ans[i - 1] in l[d[ans[i]][1]]:
    ans[i + 1] = comp(l[d[ans[i]][1]], ans[i - 1], ans[i])
else:
    ans[i + 1] = comp(l[d[ans[i]][2]], ans[i - 1], ans[i])
i += 1
while i < n - 3:
    if ans[i - 1] in l[d[ans[i]][0]] and ans[i - 2] not in l[d[ans[i]][0]]:
        ans[i + 1] = comp(l[d[ans[i]][0]], ans[i - 1], ans[i])
    elif ans[i - 1] in l[d[ans[i]][1]] and ans[i - 2] not in l[d[ans[i]][1]]:
        ans[i + 1] = comp(l[d[ans[i]][1]], ans[i - 1], ans[i])
    else:
        ans[i + 1] = comp(l[d[ans[i]][2]], ans[i - 1], ans[i])
    i += 1
print(*ans)
