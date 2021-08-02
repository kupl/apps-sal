x = int(input())


def prime_test(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for k in range(3, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True


while True:
    if prime_test(x) == True:
        print(x)
        break
    x += 1
