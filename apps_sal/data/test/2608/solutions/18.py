def whb(a, b, c, d):
    dim = (c - a + 1) * (d - b + 1)
    col1 = dim // 2
    col2 = dim - col1
    if (a + b) % 2 == 0:
        return [col2, col1]
    else:
        return [col1, col2]


def insegment(a, b, a1, b1):
    li = [[a, 1], [b, 1], [a1, 2], [b1, 2]]
    li.sort()
    if li[0][1] == li[1][1]:
        if li[1][0] == li[2][0]:
            return [li[1][0], li[2][0]]
        else:
            return -1
    else:
        return [li[1][0], li[2][0]]


def inrect(a, b, c, d, a1, b1, c1, d1):
    xra = insegment(a, c, a1, c1)
    yra = insegment(b, d, b1, d1)
    if xra == -1 or yra == -1:
        return -1
    else:
        return [xra[0], yra[0], xra[1], yra[1]]


q = int(input())
for quer in range(q):
    [n, m] = [int(i) for i in input().split()]
    [x1, y1, x2, y2] = [int(i) for i in input().split()]
    [x3, y3, x4, y4] = [int(i) for i in input().split()]
    [white, black] = whb(1, 1, n, m)
    [w1, b1] = whb(x1, y1, x2, y2)
    [w2, b2] = whb(x3, y3, x4, y4)
    black += w2 - b1
    white += b1 - w2
    inter = inrect(x1, y1, x2, y2, x3, y3, x4, y4)
    if type(inter) == list:
        [w3, b3] = whb(inter[0], inter[1], inter[2], inter[3])
        black += b3
        white -= b3
    print(white, black)
