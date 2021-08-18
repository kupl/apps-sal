def getVar():
    return tuple(map(int, input().split()))


n, m = getVar()
a = getVar()
b = getVar()
c = max(min(a) * 2, max(a))
d = min(b) - 1
if c > d:
    c = -1
print(c)
