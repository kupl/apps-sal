read = lambda: list(map(int, input().split()))
n, m = read()
f = list(read())
s = list(read())
i, j, r, x, y = 0, 0, 0, f[0], s[0]
while i < n or j < m:
    if x == y:
        i += 1
        j += 1
        if i < n and j < m:
            x, y = f[i], s[j]
        r += 1
        # print(r)
    elif x < y:
        i += 1
        x += f[i]
        # print(1, x)
    elif y < x:
        j += 1
        y += s[j]
        # print(2, y)
print(r)

