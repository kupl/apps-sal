n = int(input())
(ls, rs) = ([], [])


def check(sl):
    h = 0
    for t in sl:
        b = h + t[0]
        if b < 0:
            return False
        h += t[1]
    return True


total = 0
for i in range(n):
    (b, h) = (0, 0)
    S = input()
    for s in S:
        if s == '(':
            h += 1
        else:
            h -= 1
        b = min(b, h)
    if h > 0:
        ls.append((b, h))
    else:
        rs.append((b - h, -h))
    total += h
ls.sort(key=lambda x: x[0], reverse=True)
rs.sort(key=lambda x: x[0], reverse=True)
print('Yes' if check(ls) and check(rs) and (total == 0) else 'No')
