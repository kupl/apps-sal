n = int(input())

a = n // 7 * 2
b = a + min(n % 7, 2)
if n % 7 == 6:
    a += 1

print('{} {}'.format(a, b))
