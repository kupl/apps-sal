L = int(input())
n = len(str(bin(L))) - 3
e = []
h = 2 ** n
for i in range(1, n + 1):
    e += [(i, i + 1, 0), (i, i + 1, 2 ** (n - i))]
    if 2 ** (n - i) & L:
        e += [(1, i + 1, h)]
        h += 2 ** (n - i)
print(n + 1, len(e))
for v in e:
    print(*v)
