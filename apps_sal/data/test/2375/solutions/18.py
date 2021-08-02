x, y = map(int, input().split())
if y > x:
    x, y = y, x

if x - y <= 1:
    print("Brown")
else:
    print("Alice")
