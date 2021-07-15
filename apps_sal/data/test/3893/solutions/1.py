x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
val = 0
for i in range(int(input())):
    a, b, c = map(int, input().split())
    val += (a * x1 + b * y1 + c) * (a * x2 + b * y2 + c) < 0
print(val)
