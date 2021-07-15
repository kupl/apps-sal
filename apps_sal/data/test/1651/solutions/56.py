a, b = list(map(int, input().split()))
import math


def ok(n):
    ret = [1, n]
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ret.append(i)
            ret.append(n // i)
            if i + n // i == a:
                return "Yes"
    return "No"


print((ok(b)))


