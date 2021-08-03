a, b = map(int, input().split())
rows = [list(input()) for x in range(a)]
columns = [[x[y] for x in rows] for y in range(b)]


def check(l):
    line = []
    for x in l:
        p = x[0]
        for y in x:
            if y != p:
                break
        else:
            line.append(p)
            continue
        return [False, line]
    else:
        return [True, line]


def colors(c, l):
    p = c[1][0]
    n = 0
    colors = []
    for x in c[1]:
        if x != p:
            colors.append([p, n])
            p = x
            n = 1
        else:
            n += 1
    colors.append([p, n])
    if len(colors) == 3 and l % 3 == 0:
        m = l // 3
        letters = ["R", "G", "B"]
        for x in colors:
            p, q = x[0], x[1]
            if x[0] in letters and q == m:
                letters.remove(x[0])
            else:
                return False
                break
        else:
            return True
    else:
        return False


condition = False
if a % 3 == 0 or b % 3 == 0:
    c, d = check(rows), check(columns)
    if c[0]:
        condition = colors(c, a)
    if not condition and d[0]:
        condition = colors(d, b)
if condition:
    print("YES")
else:
    print("NO")
