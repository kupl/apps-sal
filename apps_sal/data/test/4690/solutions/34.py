a, b, c, d = map(int, input().split())

if a * b > c * d:
    print(a * b)

elif a * b < c * d:
    print(c * d)

else:
    print(a * b)
