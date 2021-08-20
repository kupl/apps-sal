import math
t = int(input())


def isprime(c):
    for x in range(2, int(math.ceil(math.sqrt(c))) + 1):
        if c % x == 0:
            return False
    return True


for x in range(t):
    (a, b) = list(map(int, input().split()))
    if 1 == a - b and isprime(a + b):
        print('YES')
    else:
        print('NO')
