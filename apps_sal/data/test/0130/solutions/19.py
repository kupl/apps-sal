def min_squares(canvas, length, width):

    def find_top():
        for i in range(length):
            for j in range(width):
                if canvas[i][j] == 'B':
                    return i
        return -1

    def find_left():
        for j in range(width):
            for i in range(length):
                if canvas[i][j] == 'B':
                    return j

    def find_bottom():
        for i in reversed(list(range(length))):
            for j in range(width):
                if canvas[i][j] == 'B':
                    return i

    def find_right():
        for j in reversed(list(range(width))):
            for i in range(length):
                if canvas[i][j] == 'B':
                    return j
    t = find_top()
    if t == -1:
        return 1
    l = find_left()
    b = find_bottom()
    r = find_right()
    painted = 0
    for i in range(t, b + 1):
        for j in range(l, r + 1):
            if canvas[i][j] == 'W':
                painted += 1
    while b - t < r - l:
        if t > 0:
            t -= 1
            painted += r - l + 1
        elif b < length - 1:
            b += 1
            painted += r - l + 1
        else:
            return -1
    while r - l < b - t:
        if l > 0:
            l -= 1
            painted += b - t + 1
        elif r < width - 1:
            r += 1
            painted += b - t + 1
        else:
            return -1
    return painted


def __starting_point():
    (l, w) = list(map(int, input().split()))
    canvas = []
    for _ in range(l):
        canvas.append(input())
    print(min_squares(canvas, l, w))


__starting_point()
