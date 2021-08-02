def get_k(a, b):
    x1, y1 = a
    x2, y2 = b
    if x2 != x1:
        return (y2 - y1) / (x2 - x1)
    return 10**10


def get_offset(a, k2):
    x, y = a
    return y - k2 * x


cnt = 0
a = []
n = int(input())
for i in range(n):
    a.append(tuple(map(int, input().split())))
alines = []
for i in range(n):
    for j in range(n):
        if i >= j:
            continue
        alines.append((a[i], a[j]))

lines = []
s = set()
for i, l1 in enumerate(alines):
    for j in range(i + 1, len(alines)):
        l2 = alines[j]
        k1, k2 = get_k(*l1), get_k(*l2)
        o1, o2 = get_offset(l1[0], k1), get_offset(l2[0], k2)
        if (k1 == k2 == 10**10 and l1[0][0] == l2[0][0]):
            o1 = o2 = 0
        if (abs(k1 - k2) < 1e-10 and abs(o1 - o2) < 1e-10) or (k1 == k2 == 10**10 and l1[0] == l2[0]):
            s.add(j)
    if i not in s:
        lines.append(l1)

for i, l1 in enumerate(lines):
    for j, l2 in enumerate(lines):
        if i >= j:
            continue
        if abs(get_k(*l1) - get_k(*l2)) > 1e-10:
            cnt += 1
print(cnt)
