from math import sqrt, floor
n = int(input())


def prime(n):
    q = floor(sqrt(n))
    prime = True
    for i in range(2, q + 1):
        if n % i == 0:
            prime = False
    return prime


if prime(n):
    print(1)
else:
    if n % 2 == 0:
        print(2)
    else:
        if prime(n-2):
            print(2)
        else:
            print(3)



