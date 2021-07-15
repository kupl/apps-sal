def try_fit(X, Y, x1, y1, x2, y2):
    if x1 > X or y1 > Y:
        return False
    newX = X - x1
    newY = Y - y1
    return (x2 <= newX and y2 <= Y) or (x2 <= X and y2 <= newY)


n, a, b = map(int, input().split())
l = []
for i in range(n):
    x, y = map(int, input().split())
    l.append((x, y))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = l[i]
        x2, y2 = l[j]
        if try_fit(a, b, x1, y1, x2, y2) or try_fit(a, b, y1, x1, x2, y2) or \
           try_fit(a, b, x1, y1, y2, x2) or try_fit(a, b, y1, x1, y2, x2):
            ans = max(ans, x1 * y1 + x2 * y2)
print(ans)
