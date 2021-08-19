import sys
import math


def ii():
    return sys.stdin.readline().strip()


def idata():
    return [int(x) for x in ii().split()]


def binary_search(array, x):
    (left, right) = (-1, len(array))
    while left + 1 != right:
        middle = (left + right) // 2
        if array[middle] >= x:
            right = middle
        elif array[middle] < x:
            left = middle
    return right


def c_mod(n1, k1, mod1):
    if mod1 != 0:
        num = den = 1
        for i in range(n1 - k1):
            num = num * (n1 - i) % mod1
            den = den * (i + 1) % mod1
        return num * pow(den, mod1 - 2, mod1) % mod1
    num = den = 1
    for i in range(n1 - k1):
        num = num * (n1 - i)
        den = den * (i + 1)
    return num // den


def v_sistemu(x, k):
    x = int(x)
    z = ''
    while x:
        z += str(x % k)
        x //= k
    return z[::-1]


def iz_sistemi(x, k):
    x = str(x)[::-1]
    ans = 0
    for i in range(len(x)):
        ans += int(x[i]) * pow(k, i)
    return ans


def solve_of_problem():
    (x, n, m) = idata()
    if x <= 10 * m:
        print('YES')
        return
    for i in range(n):
        x //= 2
        x += 10
    if 10 * m >= x:
        print('YES')
    else:
        print('NO')
    return


for ______ in range(int(ii())):
    solve_of_problem()
