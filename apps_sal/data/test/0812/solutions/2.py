n = int(input())
a = []
i = 0
for el in map(int, input().split()):
    a.append((el, i))
    i += 1
a.sort()
if n == 2:
    print(1)
    return
st = a[2][0] - a[1][0]
for i in range(1, n - 1):
    if a[i + 1][0] - a[i][0] != st:
        break
else:
    print(a[0][1] + 1)
    return
st = a[2][0] - a[0][0]
for i in range(2, n - 1):
    if a[i + 1][0] - a[i][0] != st:
        break
else:
    print(a[1][1] + 1)
    return
st = a[1][0] - a[0][0]
i = 1
found = -1
while i < n - 1:
    if a[i + 1][0] - a[i][0] != st:
        if found != -1:
            print(-1)
            return
        else:
            found = i + 1
            i += 1
    i += 1
t = a.pop(found)
for i in range(n - 2):
    if a[i + 1][0] - a[i][0] != st:
        print(-1)
        break
else:
    print(t[1] + 1)
    return

