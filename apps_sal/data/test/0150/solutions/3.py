def is_prime(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True


n = int(input())
if n % 2 == 0:
    if is_prime(n):
        print(1)
    else:
        print(2)
else:
    if is_prime(n):
        print(1)
    elif is_prime(n - 2):
        print(2)
    else:
        print(3)
