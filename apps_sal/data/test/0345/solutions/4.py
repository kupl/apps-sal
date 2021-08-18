n, m = list(map(int, input().split()))

a = []
b = []

for _ in range(m):
    aa, bb = list(map(int, input().split()))
    if (bb < aa):
        aa, bb = bb, aa
    a.append(aa)
    b.append(bb)

if (n <= 6):
    print(m)
else:

    maxv = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            alle = m
            minuse = 0
            tk = []
            for k in range(len(a)):
                if (i == a[k] and j != b[k]):
                    alle -= 1
                    tk.append(b[k])
                elif (i != a[k] and j == b[k]):
                    alle -= 1
                    tk.append(a[k])
                elif (i == b[k] and j != a[k]):
                    alle -= 1
                    tk.append(a[k])
                elif (i != b[k] and j == a[k]):
                    alle -= 1
                    tk.append(b[k])
            alle += len(set(tk))
            maxv = max(alle, maxv)
    print(maxv)
