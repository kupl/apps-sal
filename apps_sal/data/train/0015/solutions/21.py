t = int(input())
while t:
    t += -1
    a, b, x, y = map(int, input().split())
    a1 = b * x
    a2 = a * y
    a3 = b * (a - x - 1)
    a4 = a * (b - y - 1)
    print(max(a1, a2, a3, a4))
