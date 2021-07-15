def analyze(points, left_static, right_static):
    """
    (x0, +1 or -1) in points
    """

    rightest_neg = -10**9
    leftest_neg = 10**9
    rightest_pos = -10**9
    leftest_pos = 10**9
    for x, d in points:
        if d == 1:
            rightest_pos = max(rightest_pos, x)
            leftest_pos = min(leftest_pos, x)
        else:
            rightest_neg = max(rightest_neg, x)
            leftest_neg = min(leftest_neg, x)


    max_t1 = rightest_neg - right_static
    max_t2 = right_static - rightest_pos
    if max_t1 > max_t2:
        max_t1 = max_t2 = (rightest_neg-rightest_pos)/2
    max_t1 = max(0, max_t1)
    max_t2 = max(0, max_t2)
    max_x0 = max(rightest_pos, rightest_neg, right_static)
    max_x1 = max(rightest_pos + max_t1, rightest_neg - max_t1, right_static)
    def get_xmax(t):
        if t > max_t2:
            return max_x1 + t-max_t2
        elif t > max_t1:
            return max_x1
        else:
            return max_x0 - t

    min_t1 = left_static - leftest_pos
    min_t2 = leftest_neg - left_static
    if min_t1 > min_t2:
        min_t1 = min_t2 = (leftest_neg - leftest_pos)/2
    min_t1 = max(0, min_t1)
    min_t2 = max(0, min_t2)
    min_x0 = min(leftest_pos, leftest_neg, left_static)
    min_x1 = min(leftest_pos + min_t1, leftest_neg - min_t1, left_static)

    def get_xmin(t):
        if t > min_t2:
            return min_x1 - t + min_t2
        elif t > min_t1:
            return min_x1
        else:
            return min_x0 + t

    T = sorted((max_t1, max_t2, min_t1, min_t2))
    D = [get_xmax(t)-get_xmin(t) for t in T]
    return T,D



N = int(input())

conv = {'R':0,'U':1,'L':2,'D':3}
points = [(lambda i: (int(i[0]), int(i[1]), conv[i[2]]))(input().split()) for _ in range(N)]


xt, xd = analyze([(x, 1 if d == 0 else -1) for x,y,d in points if d%2==0],
                    min((x for x,y,d in points if d%2==1), default=10**9),
                    max((x for x,y,d in points if d%2==1), default=-10**9))

yt, yd = analyze([(y, 1 if d == 1 else -1) for x,y,d in points if d%2==1],
                    min((y for x,y,d in points if d%2==0), default=10**9),
                    max((y for x,y,d in points if d%2==0), default=-10**9))

def get_w(t):
    a,b,c,d = xt

    if t < a:
        return -2, xd[0] + 2*a
    elif t < b:
        return -1, xd[0] + a
    elif t < c:
        return 0, xd[1]
    elif t < d:
        return 1, xd[2] - c
    else:
        return 2, xd[3] - 2*d

def get_h(t):
    a,b,c,d = yt

    if t < a:
        return -2, yd[0] + 2*a
    elif t < b:
        return -1, yd[0] + a
    elif t < c:
        return 0, yd[1]
    elif t < d:
        return 1, yd[2] - c
    else:
        return 2, yd[3] - 2*d

T = sorted(xt+yt)

def it():
    ne = iter(T)
    next(ne)
    for a,b in zip(T,ne):
        t = (a+b)/2

        wa, wb = get_w(t)
        ha, hb = get_h(t)
        if wa*ha > 0 and a < -(wb*ha+wa*hb)/(2*wa*ha) < b:
            t = -(wb*ha+wa*hb)/(2*wa*ha)
            yield ((wa*t+wb)*(ha*t+hb), t)
        else:
            yield ((wa*a+wb)*(ha*a+hb), a)
            yield ((wa*b+wb)*(ha*b+hb), b)

print(min(it())[0])
