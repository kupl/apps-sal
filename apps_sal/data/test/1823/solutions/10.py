n, k = map(int, input().split())
lst = [*map(int, input().split())]
a, length = [lst[0]], 0
for i, x in enumerate(lst[1:]):
    if x != lst[i]:
        a.append(x)
        length += 1
d = {i: length for i in range(1, k + 1)}
d[a[0]] -= 1
for i, x in enumerate(a[1:-1]):
    if a[i] == a[i + 2]:
        d[x] -= 2
    else:
        d[x] -= 1
d[a[-1]] -= 1
res = min(d.values())
for i, x in enumerate(d):
    if d[x] == res:
        print(x)
        break
