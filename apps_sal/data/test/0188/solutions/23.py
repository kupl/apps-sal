n, k = map(int, input().split())

l = list(map(int, input().split()))

l = sorted(l, reverse=True)
s = 0
for _ in range(n):
    if l[0] <= 0:
        break
    if l[0] <= 2:
        l[0] -= min(l[0], 2)
        s += 1
    l[0] -= min(l[0], 4)
    l = sorted(l, reverse=True)
for _ in range(n):
    if l[0] <= 0:
        break
    l[0] -= min(l[0], 2)
    l = sorted(l, reverse=True)
for _ in range(n):
    if l[0] <= 0:
        break
    l[0] -= min(l[0], 2)
    l = sorted(l, reverse=True)
for _ in range(s):
    if l[0] <= 0:
        break
    l[0] -= min(l[0], 1)
    l = sorted(l, reverse=True)


if l[0] <= 0:
    print("YES")
else:
    print("NO")
