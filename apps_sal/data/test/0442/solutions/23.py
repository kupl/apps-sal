r = int(input())


def factorise(n):
    factors = []
    guess = 3
    while guess < n:
        exponent = 1
        while n % guess == 0:
            factors.append(guess ** exponent)
            n //= guess
            factors.append(n)
            exponent += 1
        guess += 2
    return sorted(factors)


if r % 2 == 1:
    x = 1
    y = (r - 3) // 2
    if y > 0:
        print(x, y)
    else:
        print('NO')
else:
    'r -= 1\n    # solve x(x + 2y + 1)\n    factors = factorise(r)\n    for x in factors:\n        y = (-x -1 + 15/x)/2\n        if y % 1 == 0:\n            print(x, y)\n            return\n    else:'
    print('NO')
