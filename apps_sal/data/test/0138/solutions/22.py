3

n, a, b, c = [int(x) for x in input().strip().split()]

if n % 4 == 0:
    print(0)
elif n % 4 == 1:
    print(min(3 * a, a + b, c))
elif n % 4 == 2:
    print(min(2 * a, b, 2 * c))
else:
    print(min(a, b + c, 3 * c))
