from functools import reduce
(a, b) = map(int, input().split())
a -= 1
print(reduce(lambda x, y: x ^ y, list(range(a - a % 4, a + 1)) + list(range(b - b % 4, b + 1))))
