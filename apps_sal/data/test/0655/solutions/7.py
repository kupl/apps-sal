n = int(input())
x, y = [int(i) for i in input().split()]

d1 = abs(x - 1) + abs(y - 1)
d2 = abs(n - x) + abs(n - y)

print("White" if d1 <= d2 else "Black")

