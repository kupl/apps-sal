3


def is_prime(x):
    if x == 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


n = int(input())
m = 1
while is_prime(n * m + 1):
    m += 1
print(m)
