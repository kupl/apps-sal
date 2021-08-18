import sys


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


l, r = list(map(int, input().split()))
for a in range(l, r - 1):
    for b in range(a + 1, r):
        for c in range(b + 1, r + 1):
            if gcd(a, b) == gcd(b, c) == 1 and gcd(a, c) != 1:
                print(a, b, c)
                return
print(-1)
