import math

l, r = [int(x)for x in input().split(' ')]

if r - l < 2:
    print(-1)
    quit()


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


for a in range(l, r + 1):
    for b in range(a + 1, r + 1):
        for c in range(b + 1, r + 1):
            if gcd(a, c) != 1 and gcd(b, c) == 1:
                print(a, b, c)
                quit()

print(-1)
