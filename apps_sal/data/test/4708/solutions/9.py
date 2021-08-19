(a, b, c, d) = [int(input()) for i in range(4)]
if a < b:
    print(a * c)
else:
    print(b * c + (a - b) * d)
