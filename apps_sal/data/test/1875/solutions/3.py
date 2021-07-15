def cross(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1

def gao():
    n = int(input())
    x, y = [], []
    for i in range(n):
        x1, y1 = input().split(' ')
        x.append(int(x1))
        y.append(int(y1))

    max_area = 0
    for i in range(n):
        for j in range(i+1, n):
            max_left, max_right = 0, 0
            for k in range(n):
                if i != k and j != k:
                    area = cross(x[j] - x[i], y[j] - y[i], x[k] - x[i], y[k] - y[i])
                    if area > 0:
                        max_left = max(max_left, area)
                    elif area < 0:
                        max_right = max(max_right, -area)
            if max_left != 0 and max_right != 0:
                max_area = max(max_area, max_left + max_right)

    print(max_area / 2.)

gao()
