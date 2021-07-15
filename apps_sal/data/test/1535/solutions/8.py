def coeff(x1, y1, x2, y2):
    a = y2 - y1;
    b = x1 - x2;
    c = -a * x1 - b * y1; 
    return (a, b, c)
    
def PointOnLine(x, y, a, b, c):
    if a * x + b * y + c == 0:
        return True
    else:
        return False

n, x0, y0 = map(int, input().split())
s = set()
x = []
y = []
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
for i in range(n):
    if (x[i], y[i]) not in s:
        a, b, c = coeff(x0, y0, x[i], y[i])
        for i in range(n):
            if PointOnLine(x[i], y[i], a, b, c):
                s.add((x[i], y[i]))
        ans += 1
print(ans)
