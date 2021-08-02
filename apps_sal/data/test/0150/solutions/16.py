import math


def tax(n):
    if n == 2:
        return 1
    if n % 2 == 0:
        return 2
    elif premier(n):
        return 1
    elif premier(n - 2):
        return 2
    else:
        return 3


def premier(k):
    if k < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(k)) + 1):
            if k % i == 0:
                return False
        return True


print(tax(int(input())))
