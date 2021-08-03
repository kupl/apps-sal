3

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input()))
l = None
r = None
i = 4
while i < n:
    if b[i] == 0 and b[i - 1] == b[i - 2] == b[i - 3] == b[i - 4] == 1:
        if r is None:
            r = min(a[i], a[i - 1], a[i - 2], a[i - 3], a[i - 4]) - 1
        else:
            r = min(r, min(a[i], a[i - 1], a[i - 2], a[i - 3], a[i - 4]) - 1)
    elif b[i] == 1 and b[i - 1] == b[i - 2] == b[i - 3] == b[i - 4] == 0:
        if l is None:
            l = max(a[i], a[i - 1], a[i - 2], a[i - 3], a[i - 4]) + 1
        else:
            l = max(l, max(a[i], a[i - 1], a[i - 2], a[i - 3], a[i - 4]) + 1)
    i += 1

if l is None:
    l = -1000000000
if r is None:
    r = 1000000000
print("%s %s" % (l, r))
