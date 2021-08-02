import sys
from math import sqrt, log, ceil
input_file = sys.stdin

n = int(input_file.readline())


def factor(n):
    lst = []
    prod = 1
    for i in range(2, n + 1):
        if n % i == 0:
            prod *= i
            lst.append(0)
            while n % i == 0:
                lst[-1] += 1
                n /= i
        if n < i:
            break
    return lst, prod


if n == 1:
    print(1, 0)
else:
    lst, ans = factor(n)
    maxi, mini = max(lst), min(lst)
    if maxi == mini and log(maxi, 2) == int(log(maxi, 2)):
        print(ans, int(log(maxi, 2)))
    else:
        print(ans, int(ceil(log(maxi, 2)) + 1))
