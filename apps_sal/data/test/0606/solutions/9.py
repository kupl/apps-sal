eps  = 0.00000000000001;
R, x1, y1, x2, y2 = map(int, input().split());
rst = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** (1/2);
#print(rst);
if rst > R:
    print(x1, y1, R- eps);
else:
    of = rst;
    #print(R, of);
    r = (R + of) / 2;
    dx = x1 - x2;
    dy = y1 - y2;
    #print(dx, dy);
    if of != 0:
        dx1 = (1/2 + R /(2 * of)) * dx;
        dy1 = (1/2 + R / (2 * of)) * dy;
    else:
        dx1 = R / 2;
        dy1 = 0;
    #print(dx1, dy1);
    x = x2 + dx1;
    y = y2 + dy1;
    print(x, y, r - eps);
