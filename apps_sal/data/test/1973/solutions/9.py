n = int(input())
a = list(map(int, input().split()))
b = [0] * 11
m = 0
b[a[0]] = 1
for i in range(1, n):
    b[a[i]] += 1
    c = set(b)
    if len(c) == 2:
        c = sorted(c)
        t = c[0] + c[1]
        if 1 in c:
            m = i
        elif b.count(t) == 1:
            m = i

    elif len(c) == 3:
        d = sorted(c)
        if d[1] == 1 and b.count(1) == 1:
            m = i
        elif d[2] - d[1] == 1 and b.count(d[2]) == 1:
            m = i


print(m + 1)
