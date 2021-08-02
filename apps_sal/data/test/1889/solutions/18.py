def fff(i):
    nonlocal a
    nonlocal m
    t = 0
    max = 0
    for j in range(m + 1):
        if a[i][j] == 0:
            if t > max:
                max = t
            t = 0
        else:
            t = t + 1
    return max


n, m, q = list(map(int, input().split()))
a = []
s = []
for i in range(0, n):
    w = list(map(int, input().split()))
    w.append(0)
    a.append(w)
    s.append(fff(i))
for i in range(q):
    x, y = list(map(int, input().split()))
    a[x - 1][y - 1] = (a[x - 1][y - 1] + 1) % 2
    s[x - 1] = fff(x - 1)
    print(max(s))
