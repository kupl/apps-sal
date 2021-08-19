(n, k) = list(map(int, input().split()))
data = input()
d = {}
c = {}
for i in data:
    if i not in c:
        c[i] = 1
    else:
        c[i] += 1
count = 0
m = 0
for i in data:
    if i not in d:
        count += 1
        d[i] = 1
        m = max(m, count)
        if d[i] == c[i]:
            del d[i]
            count -= 1
    else:
        d[i] += 1
        if d[i] == c[i]:
            del d[i]
            count -= 1
if m <= k:
    print('NO')
else:
    print('YES')
