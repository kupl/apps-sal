x, y = map(int, input().split())
a = abs(x - y)
if a == 0 or a == 1:
    print("Brown")
else:
    print("Alice")
