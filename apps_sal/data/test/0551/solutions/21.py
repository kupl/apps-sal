def coef(a, b):
    (ax, ay) = a
    (bx, by) = b
    return (by - ay) / (bx - ax)


def coefl(line):
    return coef(line[0], line[1])


def fitline(c, line):
    if len(line) <= 1:
        return True
    return coef(line[0], line[1]) == coef(line[0], c)


def same(linea, lineb):
    linec = list(lineb)
    for p in linea:
        if not fitline(p, linec):
            return False
        linec.append(p)
    return True


def allpointsfit(linea, lineb, pointset):
    for p in pointset:
        if fitline(p, linea):
            linea.append(p)
        elif fitline(p, lineb):
            lineb.append(p)
        else:
            return False
    if len(linea) == 0 or len(lineb) == 0:
        return False
    if same(linea, lineb):
        return False
    fit = len(linea) == 1 or len(lineb) == 1 or coefl(linea) == coefl(lineb)
    return fit


n = int(input())
a = [int(x) for x in input().split()]
ans = len(set(a)) == 2
points = [(idx + 1, val) for (idx, val) in enumerate(a)]
ans = ans or allpointsfit([points[0], points[1]], [points[2]], points[3:])
ans = ans or allpointsfit([points[1], points[2]], [points[0]], points[3:])
ans = ans or allpointsfit([points[0], points[2]], [points[1]], points[3:])
ans = ans or allpointsfit([], [], points)
print('Yes' if ans else 'No')
