def I():
    return map(int, input().split())


n = int(input())
a = list(I())
c = []
maxx = 0
smax = 0
for i in range(n):
    if maxx < a[i]:
        smax = maxx
        maxx = a[i]
    elif smax < a[i]:
        smax = a[i]
s = sum(a)
for i in range(n):
    if maxx != a[i]:
        if 2 * maxx == s - a[i]:
            c.append(i + 1)
    elif s - a[i] == 2 * smax:
        c.append(i + 1)
print(len(c))
print(*c)
