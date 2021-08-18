n, m = tuple(map(int, input().split()))
strings = []
for k in range(n):
    strings.append(input())


def f(x):
    if x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return "c"
    elif x in ["*", "
        return "s"
    else:
        return "l"


for k in range(n):
    strings[k] = list(map(f, strings[k]))
pointers = [1] * n
minsc = []
minss = []
minsl = []

for i in range(n):
    ds, dl, dc = -1, -1, -1
    for j in range(m):
        if strings[i][j] == "c" and (dc == -1 or min((-j) % m, j % m) < dc):
            dc = min((-j) % m, j % m)
        if strings[i][j] == "s" and (ds == -1 or min((-j) % m, j % m) < ds):
            ds = min((-j) % m, j % m)
        if strings[i][j] == "l" and (dl == -1 or min((-j) % m, j % m) < dl):
            dl = min((-j) % m, j % m)
    minsc.append(dc)
    minss.append(ds)
    minsl.append(dl)

m = -1
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k and not -1 in [minsc[i], minss[j], minsl[k]] and (minsc[i] + minss[j] + minsl[k] < m or m == -1):
                m = minsc[i] + minss[j] + minsl[k]

print(m)
