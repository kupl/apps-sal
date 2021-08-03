def calc1(x1, y1, x2, y2, x3, y3):
    a = x1 - x2
    b = y1 - y2
    c = x2 - x3
    d = y2 - y3
    if a * d - b * c == 0:
        return [0, 0, 0]
    x4 = (d * ((x1**2 + y1**2) - (x2**2 + y2**2)) - b * ((x2**2 + y2**2) - (x3**2 + y3**2))) / (2 * (a * d - b * c))
    y4 = (-c * ((x1**2 + y1**2) - (x2**2 + y2**2)) + a * ((x2**2 + y2**2) - (x3**2 + y3**2))) / (2 * (a * d - b * c))
    r = ((x1 - x4)**2 + (y1 - y4)**2)**0.5
    return [x4, y4, r]


def calc2(x1, y1, x2, y2):
    r = (((x2 - x1)**2 + (y2 - y1)**2)**0.5) / 2
    return [(x1 + x2) / 2, (y1 + y2) / 2, r]


eps = 10**(-9)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 10**18
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            cx, cy, r = calc1(arr[i][0], arr[i][1], arr[j][0], arr[j][1], arr[k][0], arr[k][1])
            for l in range(n):
                tx, ty = arr[l]
                if ((cx - tx)**2 + (cy - ty)**2) > r**2 + eps:
                    break
            else:
                ans = min(ans, r)
for i in range(n):
    for j in range(i + 1, n):
        cx, cy, r = calc2(arr[i][0], arr[i][1], arr[j][0], arr[j][1])
        for k in range(n):
            tx, ty = arr[k]
            if ((cx - tx)**2 + (cy - ty)**2) > r**2 + eps:
                break
        else:
            ans = min(ans, r)
print(ans)
