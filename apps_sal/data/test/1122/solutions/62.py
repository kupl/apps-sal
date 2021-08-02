n, m = map(int, input().split())

a = 1
b = m - 1
c = m
d = [i for i in range(n + 1)]

for i in range(m):
    if m % 2 == 0 and i < m / 2:
        print(d[a], d[a + b])
        print(d[-a - c], d[-a])
        a = a + 1
        b = b - 2
        c = c - 2

    elif m % 2 != 0 and i < m / 2:
        print(d[-a - c], d[-a])
        if i == (m + 1) / 2 - 1:
            break
        print(d[a], d[a + b])
        a = a + 1
        b = b - 2
        c = c - 2
