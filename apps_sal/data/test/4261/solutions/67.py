
a, b, c = map(int, input().split())

x = a - b

y = c - x
if c - x >= 0:
    print(y)

if c - x < 0:
    print('0')
