R = lambda: map(int, input().split())
n, l, x, y = R()
arr = set(R())
x_good, y_good = False, False
for m in arr:
    if m + x in arr or m - x in arr:
        x_good = True
        break
for m in arr:
    if m + y in arr or m - y in arr:
        y_good = True
        break
if x_good and y_good:
    print(0)
    return
elif x_good:
    print(1)
    print(y)
    return
elif y_good:
    print(1)
    print(x)
    return
else:
    for m in arr:
        if m + x <= l and (m + x + y in arr or m + x - y in arr):
            print(1)
            print(m + x)
            return
        if m - x >= 0 and (m - x + y in arr or m - x - y in arr):
            print(1)
            print(m - x)
            return
        if m + y <= l and (m + y + x in arr or m + y - x in arr):
            print(1)
            print(m + y)
            return
        if m - y >= 0 and (m - y + x in arr or m - y - x in arr):
            print(1)
            print(m - y)
            return
print(2)
print(x, y)
