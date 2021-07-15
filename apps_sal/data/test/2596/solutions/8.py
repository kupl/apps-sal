n, k, m, t = map(int, input().split())
l = [0] * n
l[k - 1] = 1
for _ in range(t):
    c, i = map(int, input().split())
    if c == 0:
        a, b = l[:i], l[i:]
        if 1 in a: l = a
        else: l = b
    else:
        l.insert(i - 1, 0)
    # print(l)
    print(len(l), l.index(1) + 1)
