(x, y) = input().split()
(x, y) = (int(x), int(y))
if x == y == 0:
    print(0)
if y >= -x and y > x:
    print(4 * y - 2)
if x + y < 0 and y >= x:
    print(4 * abs(x) - 1)
if y < x and x + y <= 1:
    print(4 * abs(y))
if x + y > 1 and y <= x:
    print(4 * x - 3)
