def merge(a, b):
    la = len(a)
    lb = len(b)
    i = 0
    j = 0
    ans = []
    while i < la and j < lb:
        if a[i] < b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1
    while i < la:
        ans.append(a[i])
        i += 1
    while j < lb:
        ans.append(b[j])
        j += 1
    return ans


n = int(input())
a = list(map(int, input().strip().split()))
d = {}
for i in range(n):
    if a[i] in d:
        d[a[i]].append(i)
    else:
        d[a[i]] = [i]
x = []
y = []
for i in d:
    x.append(i)
x.sort()
lx = len(x)
ly = 0
i = 0
j = 0
ans = {}
while i < lx or j < ly:
    r = 0
    if i >= lx:
        r = y[j]
        j += 1
    elif j >= ly:
        r = x[i]
        i += 1
    elif x[i] < y[j]:
        r = x[i]
        i += 1
    else:
        r = y[j]
        j += 1
    l = len(d[r])
    if l % 2 != 0:
        ans[d[r][-1]] = r
    if l == 1:
        continue
    temp = []
    for rj in range(1, l, 2):
        temp.append(d[r][rj])
    if 2 * r in d:
        d[2 * r] = merge(d[2 * r], temp)
    else:
        d[2 * r] = temp
        y.append(2 * r)
        ly += 1
x = []
for i in ans:
    x.append(i)
x.sort()
print(len(x))
for i in x:
    print(ans[i], end=' ')
