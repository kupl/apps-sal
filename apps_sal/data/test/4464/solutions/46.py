from math import gcd
numbers = list(map(lambda x: int(x), input().split()))
a, b, c = numbers[0], numbers[1], numbers[2]
print('YES') if not c % gcd(a, b) else print('NO')
