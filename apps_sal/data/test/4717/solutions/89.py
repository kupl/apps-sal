x, a, b = list(map(int, input().split()))

a_x = abs(a - x)
b_x = abs(b - x)

if a_x < b_x:
    print('A')
else:
    print('B')
