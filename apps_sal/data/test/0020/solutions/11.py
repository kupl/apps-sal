(h, m) = list(map(int, input().split(':')))
c = 0
while True:
    r = m % 10 * 10 + m // 10
    if r == h:
        print(c)
        break
    c += 1
    m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
