import sys
import random

def test():
    for i in range(100):
        a, b, c = [random.randint(1, 20) for _ in range(3)]
        k = 1234567 * a + 123456 * b + 1234 * c
        assert k <= 1e9
        assert solve(k) == "YES"

def solve(n):
    for i in range(811):
        for j in range(8111):
            k = 1234567 * i + 123456 * j
            if k > n:
                break
            elif (k - n) % 1234 == 0:
                return "YES"
    return "NO"

n = int(input())
print(solve(n))

