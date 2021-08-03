a, b, c = map(int, input().split())

if a > b and a > c:
    print(int(b * c / 2))
elif b > a and b > c:
    print(int(a * c / 2))
else:
    print(int(a * b / 2))
