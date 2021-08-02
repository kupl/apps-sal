a, b, c, d = list(map(int, input().split()))

rectangles_1 = a * b
rectangles_2 = c * d

if rectangles_1 > rectangles_2:
    print(rectangles_1)
else:
    print(rectangles_2)
