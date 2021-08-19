from math import floor
from fractions import Fraction
from decimal import Decimal


def com_interest(n: int) -> int:
    saving = Decimal(100)
    interest_per = 0.01
    years = 0
    while True:
        years += 1
        b = Decimal('1.01')
        saving = int(saving) * b
        if saving >= n:
            break
    return years


print(com_interest(int(input())))
