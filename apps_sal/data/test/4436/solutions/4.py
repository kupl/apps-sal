from math import sqrt


def divide(n, start):
    for k in range(start, int(sqrt(n)) + 1):
        if n % k == 0:
            return k
    return n


for _ in range(int(input())):
    n = int(input())
    a = divide(n, 2)
    if a == n:
        print('NO')
        continue
    n //= a
    b = divide(n, a + 1)
    if b == n:
        print('NO')
        continue
    n //= b
    if n <= b:
        print('NO')
        continue
    print('YES')
    print(a, b, n)
