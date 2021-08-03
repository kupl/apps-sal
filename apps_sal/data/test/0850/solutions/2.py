input()
a = list(map(int, input().split()))
d = []
for i in a:
    if i in range(1, 10):
        d += [i]
        break
for i in a:
    if i in range(10, 100, 10):
        d += [i]
        break
if len(d) == 0:
    for i in a:
        if i not in (0, 100):
            d += [i]
            break
if 100 in a:
    d += [100]
if 0 in a:
    d += [0]
print(len(d))
print(*d)
