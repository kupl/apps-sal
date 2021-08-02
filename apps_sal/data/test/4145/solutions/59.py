import math
x = int(input()) - 1


def is_prime(x):
    prime = True
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            prime = False
            break
    return prime


while True:
    x += 1
    if is_prime(x):
        print(x)
        break
