a, b, x, y = map(int, input().split())
a, b = a-1, b-1
m = up = min(2*x, y)
if a <= b:
    print(x + m*(b-a))
else:
    print(x + m*(a-b-1))
