def isPrime(n):

    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print('FastestFinger')
        continue
    if n % 2 == 1:
        print('Ashishgup')
        continue
    if n % 4 == 0:
        while n % 2 == 0:
            n = n // 2
        if n == 1:
            print('FastestFinger')
        else:
            print('Ashishgup')
        continue
    if isPrime(n // 2):
        print('FastestFinger')
    else:
        print('Ashishgup')
