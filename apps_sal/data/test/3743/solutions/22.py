import math


def smallestDivisor(n):
    # if divisible by 2
    if (n % 2 == 0):
        return 2

        # iterate from 3 to sqrt(n)
    i = 3
    while (i * i <= n):
        if (n % i == 0):
            return i
        i += 2
    return n


def isPower(div, n):
    if n == 1:
        return True
    ans = int(math.log(n, div))
    if pow(div, ans) == n or pow(div, ans + 1) == n:
        return True
    else:
        False


num = int(input().strip())
small = smallestDivisor(num)
if isPower(small, num):
    print(small)
else:
    print(1)
