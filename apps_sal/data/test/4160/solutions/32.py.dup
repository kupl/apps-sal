from decimal import Decimal


def com_interest(n: int) -> int:
    saving = 100
    interest_per = 0.01
    years = 0

    while True:
        years += 1
        saving = int(saving * Decimal('1.01'))
        if saving >= n:
            break
    return years


print(com_interest(int(input())))
