def parent(x):
    nonlocal color
    y = x
    while color[x] != x:
        x = color[x]
    while y != x:
        color[y], y = x, color[y]
    return x


def union(x, y):
    nonlocal color
    x = parent(x)
    y = parent(y)
    if size[x] < size[y]:
        x, y = y, x
    color[y] = x
    size[x] += size[y]


n, k = map(int, input().split())
a = input().split()
res = list(range(n))
color = list(range(n))
size = [1] * n
for i in range(n - k + 1):
    if a[i] == 'NO':
        union(i, i + k - 1)

alph = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
names = [x + y for x in alph.upper() for y in alph]

print(*[names[x] for x in color])
