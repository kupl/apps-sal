# E71_A

t = int(input())

for i in range(0, t):
    ln = [int(j) for j in input().split(" ")]
    b = ln[0]
    p = ln[1]
    f = ln[2]
    ln = [int(j) for j in input().split(" ")]
    h = ln[0]
    c = ln[1]
    b = b // 2
    m = 0
    if h > c:
        mn = min(b, p)
        m += mn * h
        b -= mn
        mn = min(b, f)
        m += mn * c
        b -= mn
    else:
        mn = min(b, f)
        m += mn * c
        b -= mn
        mn = min(b, p)
        m += mn * h
        b -= mn
    print(m)
