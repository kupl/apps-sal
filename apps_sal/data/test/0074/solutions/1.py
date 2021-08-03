from sys import *


def prime(a):
    if a < 2:
        return False
    for j in range(2, int(a**0.5) + 1):
        if a % j == 0:
            return False
    return True


p = [i for i in range(2, 10000) if prime(i)]
lp = len(p)

n = int(input())
if prime(n):
    print("1\n", n)
    return
if n > 3 and prime(n - 2):
    print("2\n", 2, n - 2)
    return
if n > 5 and prime(n - 4):
    print("3\n", 2, 2, n - 4)
    return

for j in range(lp):
    for i in range(j, lp):
        if p[j] + p[i] + 2 > n:
            break
        if prime(n - p[i] - p[j]):
            print("3\n", p[j], p[i], n - p[i] - p[j])
            return
