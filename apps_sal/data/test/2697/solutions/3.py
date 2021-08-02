l = []


def isPrime(n):
    if (n <= 1):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True


for _ in range(1, int(input()) + 1):
    if isPrime(_):
        l.append(_)
    else:
        pass
print(len(l))
