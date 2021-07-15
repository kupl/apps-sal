read = lambda: list(map(int, input().split()))
x1, y1 = read()
x2, y2 = read()
x3, y3 = read()
ans = 3
f1 = y1 == y2 and ((x3 >= x2 and x3 >= x1) or (x3 <= x2 and x3 <= x1))
f2 = y2 == y3 and ((x1 >= x2 and x1 >= x3) or (x1 <= x2 and x1 <= x3))
f3 = y1 == y3 and ((x2 >= x3 and x2 >= x1) or (x2 <= x1 and x2 <= x3))
f4 = x1 == x2 and ((y3 >= y2 and y3 >= y1) or (y3 <= y2 and y3 <= y1))
f5 = x2 == x3 and ((y1 >= y2 and y1 >= y3) or (y1 <= y2 and y1 <= y3))
f6 = x1 == x3 and ((y2 >= y3 and y2 >= y1) or (y2 <= y1 and y2 <= y3))
if f1 or f2 or f3 or f4 or f5 or f6: ans = 2
if x1 == x2 == x3 or y1 == y2 == y3: ans = 1
print(ans)

