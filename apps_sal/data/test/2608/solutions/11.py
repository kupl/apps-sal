from collections import defaultdict
# from fractions import Fraction
def read_line():
    return [int(x) for x in input().split()]


def solve2(n, m, x1, y1, x2, y2,
                x3, y3, x4, y4):
    def inside(x, y):
        return 1 <= x <= m and 1 <= y <= n

    def col(a, b):
        assert inside(a, b)
        return 'WB'[(a+b)%2]

    d = {}
    for i in range(1, m+1):
        for j in range(1, n+1):
            d[(i, j)] = col(i, j)
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            d[(i, j)] = 'W'
    for i in range(x3, x4+1):
        for j in range(y3, y4+1):
            d[(i, j)] = 'B'
    return len([P for P in d if d[P] == 'W']), len([P for P in d if d[P] == 'B'])

def rnd_test():
    from random import randint
    n = randint(1, 50)
    m = randint(1, 50)
    x1, x2, x3, x4 = [randint(1, m) for _ in range(4)]
    y1, y2, y3, y4 = [randint(1, n) for _ in range(4)]
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    x3, x4 = min(x3, x4), max(x3, x4)
    y3, y4 = min(y3, y4), max(y3, y4)
    assert solve(n, m, x1, y1, x2, y2,
                x3, y3, x4, y4) == solve2(n, m, x1, y1, x2, y2,
                x3, y3, x4, y4)


            
def solve(n, m, x1, y1, x2, y2,
                x3, y3, x4, y4):

    def inside(x, y):
        return 1 <= x <= m and 1 <= y <= n

    def col(a, b):
        assert inside(a, b)
        return 'WB'[(a+b)%2]

    def cols(x1, y1, x2, y2):
        assert inside(x1, y1) and inside(x2, y2)
        assert x1 <= x2 and y1 <= y2
        w, h = x2+1-x1, y2+1-y1
        if w % 2 == 0 or h % 2 == 0:
            return w*h // 2, w*h // 2
        else:
            WH, BL = w*h // 2, w*h // 2
            if col(x1, y1) == 'W':
                WH += 1
            else: BL += 1
            return WH, BL

    def overlap():
        X1 = max(x1, x3)
        X2 = min(x2, x4)
        Y1 = max(y1, y3)
        Y2 = min(y2, y4)
        if X1 > X2 or Y1 > Y2: return None
        return X1, Y1, X2, Y2

    tot_wh, tot_bl = cols(1, 1, m, n)
    # print("Starting cols: {} wh, {} bl".format(tot_wh, tot_bl))
    A_wh, A_bl = cols(x1, y1, x2, y2)
    ovrlp = overlap()
    if ovrlp is not None:
        O_wh, O_bl = cols(*ovrlp)
        assert A_wh >= O_wh and A_bl >= O_bl
        A_wh -= O_wh
        A_bl -= O_bl
        #print("Overlap cols: {} wh, {} bl".format(O_wh, O_bl))
    # print("White rect cols: {} wh, {} bl".format(A_wh, A_bl))
    B_wh, B_bl = cols(x3, y3, x4, y4)
    #print("Black rect cols: {} wh, {} bl".format(B_wh, B_bl))

    # Paint A white:
    tot_wh += A_bl
    tot_bl -= A_bl

    # Paint B black:
    tot_wh -= B_wh
    tot_bl += B_wh
    return(tot_wh, tot_bl)

# for _ in range(2000):
#     rnd_test()
# print("tested")
t = int(input())

for _ in range(t):
    n, m = read_line()
    x1, y1, x2, y2 = read_line()
    x3, y3, x4, y4 = read_line()
    print(*solve(n, m, x1, y1, x2, y2, x3, y3, x4, y4))

