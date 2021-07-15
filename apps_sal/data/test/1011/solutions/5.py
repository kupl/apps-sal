def read_pack():

    c = int(input())
    x = list(map(int, str.split(input())))
    x.sort()
    return c, x + [0]

n, a = read_pack()
m, b = read_pack()

i = j = 0
pa = pb = None
while i <= n and j <= m:

    ca = (n - i) * 3 + i * 2
    cb = (m - j) * 3 + j * 2

    if pa is None or (ca - cb > pa - pb) or (ca - cb == pa - pb and ca > pa):

        pa, pb = ca, cb

    if j == m:

        i += 1

    elif i == n:

        j += 1

    elif a[i] < b[j]:

        i += 1

    elif a[i] > b[j]:

        j += 1

    else:

        i += 1
        j += 1

print(str.format("{}:{}", pa, pb))

