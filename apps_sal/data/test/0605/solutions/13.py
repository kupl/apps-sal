a = list(map(int, input().split()))
b = a[1]
c = a[2]
d = a[3]
a = a[0]
misha = max(3 * a / 10, a - a / 250 * c)
vasya = max(3 * b / 10, b - b / 250 * d)
if misha > vasya:
    print('Misha')
elif misha == vasya:
    print('Tie')
else:
    print('Vasya')
