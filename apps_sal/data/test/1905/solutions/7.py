n, m, q = map(int, input().split())
nm = ["0"] * (m * n)
qq = [input() for _ in range(q)]
for s in reversed(qq):
    k, *l = s.split()
    if k == "3":
        nm[(int(l[0]) - 1) * m + int(l[1]) - 1] = l[2]
    elif k == "2":
        j = int(l[0]) - 1
        x = nm[j - m]
        for i in range((n - 1) * m + j, j, -m):
            nm[i] = nm[i - m]
        nm[j] = x
    else:
        j = (int(l[0]) - 1) * m
        x = nm[j + m - 1]
        for i in range(j + m - 1, j, -1):
            nm[i] = nm[i - 1]
        nm[j] = x
for i in range(0, n * m, m):
    print(' '.join(nm[i:i + m]))
