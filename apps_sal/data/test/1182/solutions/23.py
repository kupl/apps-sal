w, h, v, n = list(map(int, input().split()))
V = [[False] * h for _ in range(w)]
for _ in range(v):
    x, y = list(map(int, input().split()))
    V[x - 1][y - 1] = True


def calc(a, b, c, d):
    s = 0
    for x in range(a, c + 1):
        for y in range(b, d + 1):
            s += V[x][y];
            if s >= n: return s
    return s


C = 0
for x1 in range(w):
    for y1 in range(h):
        for x2 in range(x1, w):
            for y2 in range(y1, h):
                if calc(x1, y1, x2, y2) >= n:
                    C += 1
print(C)
