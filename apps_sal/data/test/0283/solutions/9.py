n = int(input())


def isPrime(x):
    for j in range(2, round(x ** 0.5) + 1):
        if not x % j:
            return False
    return True


for m in range(1, 1000):
    if not isPrime(m * n + 1):
        print(m)
        break
