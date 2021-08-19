(a, b, c, d) = list(map(int, input().split(' ')))
if a == c and b < d:
    print('Polycarp')
elif a == c and b > d:
    print('Vasiliy')
elif a < c and b == d:
    print('Polycarp')
elif a > c and b == d:
    print('Vasiliy')
elif a > c and b > d:
    print('Vasiliy')
elif a < c and b < d:
    print('Polycarp')
elif a + b <= max(c, d):
    print('Polycarp')
else:
    print('Vasiliy')
