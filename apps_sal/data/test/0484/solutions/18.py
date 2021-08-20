from sys import stdin as fin


def check_place(x1, y1, x2, y2, x, y):
    return x1 + x2 <= x and max(y1, y2) <= y or (max(x1, x2) <= x and y1 + y2 <= y)


(n, a, b) = map(int, fin.readline().split())
maxs = 0
rects = tuple((tuple(map(int, fin.readline().split())) for i in range(n)))
for i in range(n):
    for j in range(n):
        if i != j:
            ((x1, y1), (x2, y2)) = (rects[i], rects[j])
            if check_place(x1, y1, x2, y2, a, b) or check_place(x1, y1, y2, x2, a, b) or check_place(y1, x1, x2, y2, a, b) or check_place(y1, x1, y2, x2, a, b):
                maxs = max(maxs, x1 * y1 + x2 * y2)
                pass
print(maxs)
