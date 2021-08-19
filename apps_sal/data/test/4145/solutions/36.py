def is_prime(num):
    if num % 2 == 0 and num != 2:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


def __starting_point():
    n = int(input())
    while is_prime(n) == False:
        n += 1
    print(n)


__starting_point()
