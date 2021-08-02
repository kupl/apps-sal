from itertools import chain
# To draw square: if point isn't 'w', draw '+'


def draw_square(scr, square_a, ymin, xmin):
    for i in range(square_a + 1):
        if scr[ymin][xmin + i] != 'w':
            scr[ymin] = scr[ymin][:xmin + i] + '+' + scr[ymin][xmin + i + 1:]
        if scr[ymin + square_a][xmin + i] != 'w':
            scr[ymin + square_a] = scr[ymin + square_a][:xmin + i] + '+' + scr[ymin + square_a][xmin + i + 1:]
        if scr[ymin + i][xmin] != 'w':
            scr[ymin + i] = scr[ymin + i][:xmin] + '+' + scr[ymin + i][xmin + 1:]
        if scr[ymin + i][xmin + square_a] != 'w':
            scr[ymin + i] = scr[ymin + i][:xmin + square_a] + '+' + scr[ymin + i][xmin + square_a + 1:]
    return scr
# To find the side length of a square, and if there is some point beside the edge of a square it'll print '-1'


def find_a(pixel, y, x):
    ymax = xmax = 0
    ymin = y
    xmin = x
    ymaxl = []
    yminl = []
    xmaxl = []
    xminl = []
    count_pixel = len(pixel) // 2
    for i in range(count_pixel):
        if ymax < pixel[2 * i]:
            ymax = pixel[2 * i]
        if ymin > pixel[2 * i]:
            ymin = pixel[2 * i]
        if xmax < pixel[2 * i + 1]:
            xmax = pixel[2 * i + 1]
        if xmin > pixel[2 * i + 1]:
            xmin = pixel[2 * i + 1]
    for i in range(count_pixel):
        f = True
        if pixel[2 * i] == ymax:
            f = False
            ymaxl.append(pixel[2 * i])
            ymaxl.append(pixel[2 * i + 1])
        if pixel[2 * i] == ymin:
            f = False
            yminl.append(pixel[2 * i])
            yminl.append(pixel[2 * i + 1])
        if pixel[2 * i + 1] == xmax:
            f = False
            xmaxl.append(pixel[2 * i])
            xmaxl.append(pixel[2 * i + 1])
        if pixel[2 * i + 1] == xmin:
            f = False
            xminl.append(pixel[2 * i])
            xminl.append(pixel[2 * i + 1])
        # if some point beside the edge of a square: like the 'x'
        # 5 7
        # .......
        # .+++...
        # .+x+...
        # .www...
        # .......
        if f:
            print('-1')
            return
    return ymax, ymin, xmax, xmin, ymaxl, yminl, xmaxl, xminl


def main():
    y, x = list(map(int, input().split()))
    scr = []
    for i in range(y):
        scr.append(input())
    pixel = []
    # To collect the point info
    for i in range(y):
        for j in range(x):
            if scr[i][j] == 'w':
                pixel.append(i)
                pixel.append(j)
    ymax, ymin, xmax, xmin, ymaxl, yminl, xmaxl, xminl = find_a(pixel, y, x)
    count_ymax = len(ymaxl) / 2
    count_ymin = len(yminl) / 2
    count_xmax = len(xmaxl) / 2
    count_xmin = len(xminl) / 2
    countx_ymax = ymaxl[1::2].count(xmax) + ymaxl[1::2].count(xmin)
    countx_ymin = yminl[1::2].count(xmax) + yminl[1::2].count(xmin)
    county_xmax = xmaxl[::2].count(ymax) + xmaxl[::2].count(ymin)
    county_xmin = xminl[::2].count(ymax) + xminl[::2].count(ymin)
    # print('ymax:%d,ymin:%d,xmax:%d,xmin:%d'%(ymax,ymin,xmax,xmin))
    # print(f'ymaxl:\n{ymaxl}\nyminl:\n{yminl}\nxmaxl:\n{xmaxl}\nxminl:\n{xminl}\ncounty_xmax:{county_xmax}\ncounty_xmin:{county_xmin}\ncountx_ymax:{countx_ymax}\ncountx_ymin:{countx_ymin}')
    # There are three conditions:
    # 1.height > width  2.height < width    3.height == width
    # eg: 1.height > width:
    # so square_a = height
    if ymax - ymin > xmax - xmin:
        square_a = ymax - ymin
        # if the point form a rectangle:
        # 5 7
        # .......
        # .ww....
        # .wx....
        # .ww....
        # .......
        # or
        # 5 7
        # .......
        # .w.....
        # .w.....
        # .w.....
        # .......
        if county_xmax < count_xmax and county_xmin < count_xmin:
            # 5 7
            # .......
            # .w++...
            # .w.+...
            # .w++...
            # .......
            if xmax == xmin:
                if xmin + square_a < x:
                    xmax = xmin + square_a
                elif xmax - square_a >= 0:
                    xmin = xmax - square_a
                else:
                    print('-1')
                    return
            else:
                print('-1')
                return
        # if the point from the shape of [ like:
        # 5 7
        # .......
        # .www...
        # .w.....
        # .www...
        # .......
        elif county_xmax < count_xmax and county_xmin == count_xmin:
            xmin = xmax - square_a
            if xmin < 0:
                print('-1')
                return
        # if the point from the shape of ] like:
        # 5 7
        # .......
        # .www...
        # ...w...
        # .www...
        # .......
        elif county_xmax == count_xmax and county_xmin < count_xmin:
            xmax = xmin + square_a
            if xmax >= x:
                print('-1')
                return
        # if there is some point to make county_xmax == count_xmax and county_xmin == count_xmin like:
        # 5 7
        # .......
        # .w.....
        # .......
        # ..w....
        # .......
        elif county_xmax == count_xmax and county_xmin == count_xmin:
            if square_a < x:
                if xmin + square_a < x:
                    xmax = xmin + square_a
                elif xmax - square_a >= 0:
                    xmin = xmax - square_a
                # sp:
                # 5 5
                # .w...
                # .....
                # .....
                # .....
                # ..w..
                else:
                    xmin = 0
                    xmax = xmin + square_a
            else:
                print('-1')
                return
    elif ymax - ymin < xmax - xmin:
        square_a = xmax - xmin
        if countx_ymax < count_ymax and countx_ymin < count_ymin:
            if ymax == ymin:
                if ymin + square_a < y:
                    ymax = ymin + square_a
                elif ymax - square_a >= 0:
                    ymin = ymax - square_a
                else:
                    print('-1')
                    return
            else:
                print('-1')
                return
        elif countx_ymax < count_ymax and countx_ymin == count_ymin:
            ymin = ymax - square_a
            if ymin < 0:
                print('-1')
                return
        elif countx_ymax == count_ymax and countx_ymin < count_ymin:
            ymax = ymin + square_a
            if ymax >= y:
                print('-1')
                return
        elif countx_ymax == count_ymax and countx_ymin == count_ymin:
            if square_a < y:
                if ymin + square_a < y:
                    ymax = ymin + square_a
                elif ymax - square_a >= 0:
                    ymin = ymax - square_a
                else:
                    ymin = 0
                    ymax = ymin + square_a
            else:
                print('-1')
                return
    elif ymax - ymin == xmax - xmin:
        square_a = xmax - xmin
    # print('ymax:%d,ymin:%d,xmax:%d,xmin:%d,a:%d'%(ymax,ymin,xmax,xmin,square_a))
    scr = draw_square(scr, square_a, ymin, xmin)
    for i in range(y):
        print(scr[i])


def __starting_point():
    main()
    # while True:
    #    main()


__starting_point()
