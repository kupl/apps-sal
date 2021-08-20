(a, b, c, d) = list(map(int, input().split(' ')))
Vasya = max(3 * b / 10, b - b / 250 * d)
Misha = max(3 * a / 10, a - a / 250 * c)
if Vasya > Misha:
    print('Vasya')
elif Misha > Vasya:
    print('Misha')
else:
    print('Tie')
