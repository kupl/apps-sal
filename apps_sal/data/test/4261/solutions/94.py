a, b, c = map(int, input().split())

f1 = a - b
f2 = c - f1

if f2 <= 0:
    print('0')
else:
    print(f2)
