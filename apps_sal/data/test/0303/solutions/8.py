x1, y1, x2, y2 = list(map(int, input().split()))
x, y = list(map(int, input().split()))

a = (x2 - x1) // x
b = (y2 - y1) // y

if a % 2 == b % 2 and (x2 - x1) % x == 0 and (y2 - y1) % y == 0:
    print("YES")
else:
    print("NO")


