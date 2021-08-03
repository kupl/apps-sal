n = int(input())

fibs = set()

a, b = 1, 1
while a <= 1000:
    a, b = b, a + b
    fibs.add(a)

print(''.join('O' if i in fibs else 'o' for i in range(1, n + 1)))
