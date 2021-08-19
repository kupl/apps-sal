def check(x, y, a, b):
    return min(x, y) <= min(a, b) and max(x, y) <= max(a, b)


(n, a, b) = list(map(int, input().split()))
p = []
for i in range(n):
    (xi, yi) = list(map(int, input().split()))
    p.append((xi, yi))
ans = 0
for i in range(n):
    for j in range(i):
        (x1, y1) = p[i]
        (x2, y2) = p[j]
        if check(max(x1, x2), y1 + y2, a, b) or check(max(x1, y2), x2 + y1, a, b) or check(max(y1, x2), x1 + y2, a, b) or check(max(y1, y2), x1 + x2, a, b):
            ans = max(ans, x1 * y1 + x2 * y2)
print(ans)
