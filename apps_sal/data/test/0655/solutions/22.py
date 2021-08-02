n = int(input())
x, y = map(int, input().split())
a = max(abs(1 - x), abs(1 - y))
b = max(abs(n - x), abs(n - y))
if a <= b:
    print("White")
else:
    print("Black")
